import { render, screen, fireEvent } from "@testing-library/svelte"

import Home from "./Home.svelte"

descirbe("Home", () => {
    render(Home)
    const node = screen.queryByText("This is football!")
    expect(node).not.toBeNull()    
})

