<script lang="ts">
    import {push, pop, replace } from "svelte-spa-router";
    import { st_team, st_fixtures, st_teams } from "../store.js";
    import * as d3 from 'd3';
    import { fly } from "svelte/transition";
    import Axis from "../Axis.svelte";

    export let params = {};
    
    let datasetX = [];
    let dataset2 = [];
    let team;
    let fixtures = [];

    function start_process() { 
        if(!team){
            fetch("https://wta-project-football.azurewebsites.net/api/team/" + params["id"] + "/")
            .then(response => response.json()) 
            .then(data => {
                team = data;
                st_team.set(data);
            }).catch(error => {
                console.log(error);
                return [];
            });   
        }

        fetch("https://wta-project-football.azurewebsites.net/api/lineups/" + params["id"] + "/")
        .then(response => response.json()) 
        .then(data => {
            dataset2 = data;
        }).catch(error => {
            console.log(error);
            return [];
        });

        fetch("https://wta-project-football.azurewebsites.net/api/fixtures/" + params["id"] + "/?format=json")
        .then(response => response.json()) 
        .then(data => {
            make_dataset2(data);           
        }).catch(error => {
            console.log(error);
            return [];
        });

        st_fixtures.subscribe(val => {
            fixtures = val;
        });
    }

    const go_home = () => {
        st_teams.set([]);
        push("/");
    }

    type Enemy = {
        id: number,
        name: string,
        icon: string
    }

    type Fixture = {
        "id": number,
        "referee": string,
        "date": string,
        "venue": string,
        "status": string,
        "home_goals": number,
        "away_goals": number,
        "home_team": number,
        "away_team": number
    }

    function make_dataset2(data) {
        let ids = [];
        let fs = [];
        fixtures = [];
        st_fixtures.set(fixtures);

        data.forEach(fixture => {
            ids.push(get_enemy_id(fixture));
            fs.push(fixture)
        })  

        do_next(fs, ids);
    }

    async function do_next(fs, ids) {
        console.log(fs);
        console.log(ids);

        for (let i = 0; i < fs.length; i++) {
            await fetch("https://wta-project-football.azurewebsites.net/api/team/"+ ids[i] + "/?format=json")
            .then(response => response.json()) 
            .then(enemy => {
                finish_dataset(fs[i], enemy);
            }).catch(error => {
                console.log(error);
                return [];
            });
        }
    }

    function get_enemy_id(fixture: Fixture) {
        if(fixture.home_team == params["id"]) {
            return fixture.away_team;
        } else {
            return fixture.home_team;
        }
    }

    function finish_dataset(fixture: Fixture, enemy: Enemy) {
        let team_goals = 0;
        let enemy_goals = 0;

        if(fixture.home_team == params["id"]) {
            team_goals = fixture.home_goals;
            enemy_goals = fixture.away_goals;
        } else {
            enemy_goals = fixture.home_goals;
            team_goals = fixture.away_goals;
        }

        let result = "";

        if(enemy_goals > team_goals) {
            result = "Loss";
        } else if(enemy_goals == team_goals) {
            result = "Draw";
        } else {
            result = "Win";
        }

        if(fixture.status === "Match Finished"){
            let data = {
                enemy_name: enemy.name,
                enemy_icon: enemy.icon,
                team_goals: team_goals,
                enemy_goals: enemy_goals,
                result: result
            }

            fixtures.push(data);
            st_fixtures.set(fixtures);
            datasetX.push(data.enemy_name);
        }
    }

    const margin = { top: 50, bottom: 50, left: 50, right: 50 };
    const width = 900, height = 500;

    const  innerHeight  =  height  -  margin.top  -  margin.bottom,
    innerWidth  =  width  -  margin.left  -  margin.right;

    $: xScale = d3.scaleBand()
        .domain(dataset2.map((d) => d.formation))
        .range([0, innerWidth])
        .padding(0.3);

    $: yScale = d3.scaleLinear()
        .domain([0, d3.max(dataset2, (d) => d.played + 2)])
        .range([innerHeight, 0]);
    
    $: x2Scale  =  d3.scalePoint()
        .domain(fixtures.slice(-5).map(f => f.enemy_name))
        .range([0, innerWidth])
        .padding(1); 

    $: y2Scale  =  d3.scalePoint()
        .domain(["Win", "Draw", "Loss"])
        .range([0, innerHeight])
        .padding(1);

    const classSet = new Set(["Win", "Draw", "Loss"]);
    $: colorScale = d3.scaleOrdinal()
        .domain(classSet)
        .range(["#146714", "#eef5f7", "#671414"]);
</script>

<style lang="scss">
    $color-white: #eef5f7;
    $color-lightblue: #2E9CCA;
    $color-darkblue: #00385b;
    $color-background-opacity: rgba(20, 71, 104, 0.8);
    $color-box-shadow: rgba(0,0,0,0.07);
    $text-size: 1.2em;
    $margin: 3em;

    h2 {
        color: $color-white;
        font-size: 1.8em;
    }
    
    .title {
        margin-left: $margin;
        margin-top: $margin;
        display: flex;
        flex-direction: row;
        
        .title-group {
            display: flex;
            flex-direction: column;
            align-items: flex-start;

            h1 {
                color: $color-white;
                font-size: 2.4em;
            }

            .back {
                background: none;
                border: none;
                padding: 0;
                color: $color-white;
                cursor: pointer;
                font-size: $text-size;
            }
        }

        #image_team {
            margin-left: 2em;
        }
    }

    .container-info {
        margin-left: $margin;
        margin-top: $margin;

        .container-form {
            width: 100%;

            svg {
                max-width: 60em;
                background: $color-background-opacity;
                box-shadow: 0 1px 2px $color-box-shadow, 
                        0 2px 4px $color-box-shadow, 
                        0 4px 8px $color-box-shadow, 
                        0 8px 16px $color-box-shadow,
                        0 16px 32px $color-box-shadow, 
                        0 32px 64px $color-box-shadow; 
            }
        }
    }

    .container {
        display: flex;
        flex-direction: row;
        margin: $margin;
        @media screen and (max-width : 1500px){
            flex-direction: column;

            .container-matches {
                width: 60em;
                margin-top: $margin;
            }
        }

        .container-graph {
            max-width: 60em;
            align-self: flex-top;

            svg {
                height:35em;
                padding:2em;
                background: $color-background-opacity;
                box-shadow: 0 1px 2px $color-box-shadow, 
                        0 2px 4px $color-box-shadow, 
                        0 4px 8px $color-box-shadow, 
                        0 8px 16px $color-box-shadow,
                        0 16px 32px $color-box-shadow, 
                        0 32px 64px $color-box-shadow; 
            }

            rect {
                fill: $color-white;
            }
        }

        .container-matches {
            align-self: flex-top;
            margin-left: 1em;
            
            .list-container {
                max-height:35em;
                padding:2em;
                background: $color-background-opacity;
                box-shadow: 0 1px 2px $color-box-shadow, 
                        0 2px 4px $color-box-shadow, 
                        0 4px 8px $color-box-shadow, 
                        0 8px 16px $color-box-shadow,
                        0 16px 32px $color-box-shadow, 
                        0 32px 64px $color-box-shadow;   
                overflow-y:scroll;  

                .list {
                    list-style-type: none;
                    margin: 0;
                    padding: 0;
                    text-align: center;  
                    
                    .match {
                        margin: 1em;
                        padding: 0.5em;
                        height: $text-size;
                        font-size: $text-size;
                        background: $color-darkblue;
                        color: $color-white;
                        box-shadow: 0 1px 2px $color-box-shadow, 
                                0 2px 4px $color-box-shadow, 
                                0 4px 8px $color-box-shadow, 
                                0 8px 16px $color-box-shadow,
                                0 16px 32px $color-box-shadow, 
                                0 32px 64px $color-box-shadow; 
                        text-align: left;

                        .icon {
                            width: auto;
                            height: 100%;
                        }
                    }
                }
            }
        }
    }

</style>

{#if team}
    <section class="title">
        <div class="title-group">
            <h1>{team.name}</h1>
            <button class="back" on:click={(go_home)}>Back to leaderboard</button>
        </div>
        <img id="image_team" src={team.icon} alt="This is the logo of {team.name}"/>
    </section>
{:else}
    {start_process()}
{/if}

<section class="container-info">
    <div class="container-form">
        <h2>Form last 5 games</h2>
        <svg width=1200 height=500>
            <g  transform={`translate(${50},${50})`}>
                {#each fixtures.slice(-5) as f}
                    <circle 
                        cx={x2Scale(f.enemy_name)}
                        cy={y2Scale(f.result)}
                        r="20"
                        style={`fill:${colorScale(f.result)}`}
                    />
                {/each}
                <Axis  {innerHeight}  {margin}  scale={x2Scale}  position="bottom" />
                <Axis  {innerHeight}  {margin}  scale={y2Scale}  position="left" />
            </g>
        </svg>
    </div>
</section>


<section class="container">
    <div class="container-graph">
        <h2>Times each formation is used</h2>
        <svg {width} {height}>
            <g  transform={`translate(${50},${50})`}>
                {#each dataset2 as data, i}
                    <rect
                        x={xScale(data.formation)}
                        y={yScale(data.played)}
                        width={xScale.bandwidth()}
                        height={(innerHeight - yScale(data.played))}
                        in:fly={{ y: 100, duration: 1000, delay: i * 100 }}
                    />
                {/each}
                <text fill="#eef5f7" transform={`translate(${-30},${innerHeight/2}) rotate(-90)`}
                    >Amount of times
                </text>
                <text fill="#eef5f7" x={innerWidth  /  2  }  y={innerHeight  +  35}>Formation</text>
                <Axis  {innerHeight}  {margin}  scale={xScale}  position="bottom" />
                <Axis  {innerHeight}  {margin}  scale={yScale}  position="left" />
            </g>
        </svg>
    </div>

    <div class="container-matches">
        <h2>Played matches</h2>
        <div class="list-container">
            <ul class="list">            
                {#each fixtures as fixture}
                    {#if team}
                        <li class="match">{fixture.team_goals}:{fixture.enemy_goals} | 
                            <img class="icon" src={team.icon} alt="This is the logo of {team.name}"/> 
                            VS 
                            <img class="icon" src={fixture.enemy_icon} alt="This is the logo of {fixture.enemy_name}"/> 
                            {fixture.enemy_name}
                        </li>
                    {/if}
                {/each}
            </ul>
        </div>
    </div>
</section>




