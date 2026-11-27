---
name: figcraft-canvas
description: Work with a collaborator on an explicitly selected FigCraft canvas during Shape, and save a reviewable design revision.
---

# FigCraft Canvas

Use the assigned FigCraft MCP connection. Confirm the open file and target page or frame using `inspect_document`. Pass the explicit `document` ID or open file path on every supported call, including inspection, edits, exports, and saves. If the MCP connection is unavailable, ask the collaborator to open the project’s configured FigCraft session on the runtime Mac. If the connection works but the target file is closed or unclear, ask them to open or identify that file. Give the exact project-relative file and ask them to reply when it is ready. Keep the issue in its current stage and end the run after the request. Resume on the collaborator’s reply and confirm the target before editing. Launching a desktop app requires separately approved launch instructions. A tool that depends on the front tab needs exclusive use of the app for that operation.

Agents may overlap through the same attached MCP connection when each has its own open file. Keep one writer per editable document, including across pages. If two agents need to edit the same file, sequence their work or use separate working files and let the design owner integrate the accepted changes.

Keep batches focused. FigCraft queues commands on its UI thread, so a long batch can delay other clients. If a call fails or times out, re-inspect the same explicit document before retrying a write because the app may already have applied it. Use the allowed project folder for saves and exports.

Keep one editable canvas file for the issue. Save edits there and use named pages for alternatives or meaningful working versions. During ordinary collaboration, point to the live page or frame. Use zero attachments and save edits to the existing file. Skip frozen copies, PNG exports, galleries, and version uploads after routine edits. For a specific visual question, attach at most one focused crop when the live canvas reference is insufficient, or provide the visual the collaborator explicitly requests. Internal inspection is separate from publishing. Use targeted inspection and batch related edits where practical.

Only at a formal handoff, save one frozen native snapshot, the minimum tool-independent preview needed to review it, and decision notes. Record the native snapshot and preview paths on the issue when the reviewer can access the project. Prefer an existing shared link for other recipients. Attach the minimum needed only when access, preservation, or an explicit request calls for it. Reuse it if the revision is unchanged. The Shape owner publishes the approval packet as soon as the material design choices are settled and the design is ready.
