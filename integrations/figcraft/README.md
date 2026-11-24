# FigCraft integration

Use FigCraft for live canvas work when a Shape issue selects it. The [Shape workflow](../../workflows/README.md) and [Shape skill](../../skills/shape-product/SKILL.md) define the expected outcome. The [FigCraft tooling skill](../../skills/figcraft-canvas/SKILL.md) covers the canvas operations. Another design tool can use the same issue handoff with its own integration and tooling skill.

## Set up the local connection

1. Install the CLI from the [official FigCraft releases](https://github.com/storytold/figcraft/releases), matching the desktop app's version. On macOS the CLI is a separate download. Register its absolute installed path with the orchestrator because the runtime may have a different PATH.
2. Use the existing human project checkout's ignored `.local/design/` directory. In SynThesis this is `~/workspace/SynThesis/.local/design`. Keep it out of Git with a local exclude for `/.local/design/`. Set `design_root` to its absolute path and launch FigCraft with the control port and automation roots. The folder must exist on the same machine as the Product & Design runtime.

   ```sh
   open -n -a /Applications/FigCraft.app --args --control 7979 \
     --automation-read-root "$design_root" --automation-write-root "$design_root"
   ```

3. Register a local stdio MCP server with the orchestrator. Use the CLI's absolute path as the command and `mcp`, `--attach`, and `7979` as separate arguments. Assign the connection and FigCraft tooling skill to the design role. The orchestrator starts the CLI on the runtime machine, and FigCraft holds the live canvas. Quit the controlled FigCraft window when finished and launch it the same way for the next session.
4. Verify on a scratch canvas before editing a product issue. Inspect the document, make one named edit, export a PNG, and confirm the file save stays in the project design folder. Remove the scratch test files when done. The attached app enforces the roots itself. Its control listener is loopback-only and the rooted session disables FigCraft sharing. [FigCraft MCP reference](https://github.com/storytold/figcraft/blob/v0.18.1/docs/mcp.md#confining-file-access)

Use one controlled document or clearly identified tab per issue. If the app is closed or the intended document is unavailable, report that in the issue and wait for the collaborator to open it before attempting live edits.

## Multica wiring

Add `figcraft-synthesis` in **Workspace Settings → MCP** using the stdio configuration above. Assign the workspace MCP entry and FigCraft tooling skill only to Product & Design. Follow the [workspace library rules](../multica/README.md#workspace-skills-and-mcp-servers) to remove a duplicate after verifying the library assignment.

## Hand off a design revision

Keep editable working files in the local design folder. Give each review revision its own snapshot and pair it with PNG or PDF previews and the decision notes. Attach the preview and notes to the issue, with the native snapshot when another session needs to reopen it. Use the issue artifact or another accessible versioned reference when approval must identify exactly what was reviewed. Keep exploratory files out of the product repository's published history.

Mike approves the revision by moving the issue to Plan Delivery. Delivery should be able to read the review packet without signing into a particular design tool.
