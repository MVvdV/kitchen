# FigCraft integration

Use FigCraft for live canvas work when a Shape issue selects it. The [Shape workflow](../../workflows/README.md) and [Shape skill](../../skills/shape-product/SKILL.md) define the expected outcome. The [FigCraft tooling skill](../../skills/figcraft-canvas/SKILL.md) covers the canvas operations. Another design tool can use the same issue handoff with its own integration and tooling skill.

## Set up the local connection

1. Install the CLI from the [official FigCraft releases](https://github.com/storytold/figcraft/releases), matching the desktop app's version. On macOS the CLI is a separate download. Register its absolute installed path with the orchestrator because the runtime may have a different PATH.
2. Use the existing project checkout's visible `artifacts/` directory. In SynThesis this is `~/workspace/SynThesis/artifacts`. Exclude `/artifacts/` from Git in the local checkout. Set `design_root` to the absolute artifact root and launch FigCraft with the control port and automation roots. The folder must exist on the same machine as the Product & Design runtime.

   ```sh
   open -n -a /Applications/FigCraft.app --args --control 7979 \
     --automation-read-root "$design_root" --automation-write-root "$design_root"
   ```

3. Register a local stdio MCP server with the orchestrator. Use the CLI's absolute path as the command and `mcp`, `--attach`, and `7979` as separate arguments. Assign the connection and FigCraft tooling skill to the design role. The orchestrator starts the CLI on the runtime machine, and FigCraft holds the live canvas. Quit the controlled FigCraft window when finished and launch it the same way for the next session.
4. Verify on a scratch canvas before editing a product issue. Inspect the document, make one named edit, export a PNG, and confirm the file save stays in the project design folder. Remove the scratch test files when done. The attached app enforces the roots itself. Its control listener is loopback-only and the rooted session disables FigCraft sharing. [FigCraft MCP reference](https://github.com/storytold/figcraft/blob/v0.18.1/docs/mcp.md#confining-file-access)

Use one controlled document or clearly identified tab per issue. Save to `artifacts/<issue-id>/design/` and target the document by ID on tool calls, so a tab change or another issue's run does not redirect edits. Keep one agent writer per editable document. For a shared prototype, keep the canonical file with its owning issue and link to that exact revision from contributing issues. See the [project directory rules](../../workflows/project-directories.md#prototypes-shared-across-issues). If the app is closed or the intended document is unavailable, report that in the issue and wait for the collaborator to open it before attempting live edits.

## Concurrent agent work

The attached FigCraft 0.18.1 control channel accepts several clients and queues their commands on the app’s UI thread. Two Multica runs can overlap through one workspace MCP entry when each writer has its own open file. A long batch can delay another run’s commands. Keep the app’s project-folder restrictions in place for this setup. [FigCraft control protocol](https://github.com/storytold/figcraft/blob/v0.18.1/docs/control-protocol.md)

1. Give each agent a distinct editable file under the owning issue’s design folder and keep both files open in the controlled app. Record the exact file and writing owner on each issue.
2. Have each agent confirm its file and pass the explicit `document` ID or open file path on supported calls, particularly edits, exports, and saves. Calls without a document target can follow the front tab. If a required operation uses the front tab, coordinate exclusive app use for that operation. [FigCraft document targeting](https://github.com/storytold/figcraft/blob/v0.18.1/docs/mcp.md#naming-the-document)
3. Keep one writer per editable file. Named pages organize work within a file and do not isolate writers. For work on one file, schedule turns or use separate working files and let the owning designer integrate accepted changes.
4. Keep command batches focused. After a timeout, re-inspect the explicit target before retrying, since the previous write may already have landed.

## Multica wiring

Add `figcraft-synthesis` in **Workspace Settings → MCP** using the stdio configuration above. Assign the workspace MCP entry and FigCraft tooling skill only to Product & Design. Follow the [workspace library rules](../multica/README.md#workspace-skills-and-mcp-servers) to remove a duplicate after verifying the library assignment.

## Hand off a design revision

Keep one editable FigCraft file in `artifacts/<issue-id>/design/`. Use named pages for alternatives or meaningful working versions and refer to those pages in conversation. Keep routine replies attachment-free and refer to the page or frame. Share one focused crop when that specific question depends on it and the canvas reference is insufficient. Skip saved copies and review exports during ordinary edits. For a formal handoff, save one frozen native snapshot, a focused tool-independent preview, and decision notes in `artifacts/<issue-id>/review/`. Link the exact packet on the issue. Use the issue artifact or another accessible versioned reference when approval must identify exactly what was reviewed. Keep exploratory files out of the product repository's published history.

Mike approves the revision by moving the issue to Plan Delivery. Delivery should be able to read the review packet without signing into a particular design tool.
