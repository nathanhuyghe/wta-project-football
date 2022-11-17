<script>
    import Axis from "../Axis.svelte";
    import * as d3 from 'd3';
    
    let dataset = [];
    const margin = { top: 50, bottom: 50, left: 50, right: 50 };
    const width = 900,height = 500;

    const  innerHeight  =  height  -  margin.top  -  margin.bottom,
    innerWidth  =  width  -  margin.left  -  margin.right;

    $: xScale  =  d3.scaleLinear()
        .domain(d3.extent(dataset, (d)  =>  d.day))
        .range([0, innerWidth]);

    $: yScale  =  d3.scaleLinear()
        .domain(d3.extent(dataset, (d)  =>  d.placement))
        .range([0, innerHeight]);

    const classSet = new Set(dataset.map((d) => d.enemy_name));
    $: colorScale = d3.scaleOrdinal()
        .domain(classSet)
        .range(["#003049", "#d62828", "#f77f00", "black", "red", "green", "purple", "blue", "pink", "yellow"]);

    $: line_gen  =  d3.line()
        .curve(d3.curveNatural)
        .x((d)  =>  xScale(d.day))
        .y((d)  =>  yScale(d.placement))(dataset);
</script>


<svg {width} {height}>
    <g  transform={`translate(${50},${50})`}>
        {#each dataset as data}
            <circle
                cx={xScale(data.day)}
                cy={yScale(data.placement)}
                r="7.5"
                style={`fill:${colorScale(data.enemy_name)}`}
            />
        {/each}
        <text fill="#eef5f7" transform={`translate(${-30},${innerHeight  /  2}) rotate(-90)`}
            >Placement
        </text>
        <text fill="#eef5f7" x={innerWidth  /  2  }  y={innerHeight  +  35}>Day</text>
        <path  d={line_gen} />
        <Axis  {innerHeight}  {margin}  scale={xScale}  position="bottom" />
        <Axis  {innerHeight}  {margin}  scale={yScale}  position="left" />
    </g>
</svg>