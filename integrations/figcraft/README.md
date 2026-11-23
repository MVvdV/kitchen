# FigCraft integration

Use FigCraft for live canvas work when a Shape issue selects it. The [Shape workflow](../../workflows/README.md) and [Shape skill](../../skills/shape-product/SKILL.md) define the expected outcome. The [FigCraft tooling skill](../../skills/figcraft-canvas/SKILL.md) covers the canvas operations. Another design tool can use the same issue handoff with its own integration and tooling skill.

## Set up the local connection

1. Install the CLI from the [official FigCraft releases](https://github.com/storytold/figcraft/releases), matching the desktop app's version. On macOS the CLI is a separate download. Use its absolute installed path in Multica because the runtime may have a different PATH.
2. Create a dedicated local design folder for the project and launch FigCraft with the control port and automation roots. On macOS, use the following command after setting `design_root` to the absolute design folder. The existing folder must be on the same machine as the Product & Design runtime.

   ```sh
   open -n -a /Applications/FigCraft.app --args --control 7979 \
     --automation-read-root "$design_root" --automation-write-root "$design_root"
   ```

3. Configure a local stdio server for Product & Design. Set the command to the CLI's absolute path and arguments to `mcp --attach 7979`. Use the agent's private MCP configuration for a single agent, or register the server in Multica's MCP library and assign it only to that agent. Assign the FigCraft tooling skill to the same agent. The daemon starts the CLI in each run. The desktop app stays open under the human's control. Quit the controlled FigCraft window when finished and launch it the same way for the next session.
4. Verify on a scratch canvas before editing a product issue. Inspect the document, make one named edit, export a PNG, and confirm the file save stays in the project design folder. The attached app enforces the roots itself. Its control listener is loopback-only and the rooted session disables FigCraft sharing. [FigCraft MCP reference](https://github.com/storytold/figcraft/blob/v0.18.1/docs/mcp.md#confining-file-access)

Use one controlled document or clearly identified tab per issue. If the app is closed or the intended document is unavailable, report that in the issue and wait for the collaborator to open it before attempting live edits.

## Hand off a design revision

Keep editable working files in the local design folder. Give each review revision its own snapshot and pair it with PNG or PDF previews and the decision notes. Attach the preview and notes to the issue, with the native snapshot when another session needs to reopen it. Use the issue artifact or another accessible versioned reference when approval must identify exactly what was reviewed. Keep exploratory files out of the product repository's published history.

Mike approves the revision by moving the issue to Plan Delivery. Delivery should be able to read the review packet without signing into a particular design tool.
