# Project directory management

Use one visible project root as the place people find the repository and working artifacts. Keep the layout independent of the issue tracker, agent runtime, and design tool. Each integration documents how its tools locate the project root and the managed checkout.

## Layout

| Location | What belongs there |
| --- | --- |
| Project root | The human checkout and one visible `artifacts/` directory. |
| Product repository and isolated Git worktrees | Implementation, tests, authoritative briefs under `docs/product/`, issue specs under `docs/specs/<issue-id>/`, and architecture decisions under `docs/adr/`. |
| `artifacts/<issue-id>/intake/` | Local copies of source inputs. Link the source snapshot on the issue. |
| `artifacts/<issue-id>/design/` | Editable design files, exploratory prototypes, and any code or instructions required to run them. |
| `artifacts/<issue-id>/review/` | Named, revisioned previews, snapshots, and verification evidence. |
| Run-scoped temporary storage | Rebuildable dependencies, caches, and temporary output that need only live for one run. Clean up what you created before ending the run. |

Ignore `/artifacts/` in Git. Create issue subfolders only as needed. Use the orchestrator's managed worktree for code and the existing project artifact root for local design work. Ask before creating sibling directories in the workspace.

## Prototypes shared across issues

Every editable prototype has one owning issue. Put the canonical working copy under that issue's `design/` folder. Other issues link to the owner and the exact revision they used. Keep their variants and evidence in their own issue folders. For concurrent work, give variants separate files and use one agent writer per editable file. The owning issue consolidates accepted changes into the next revision and records the contributing issue links.

An exploratory code prototype stays under the owning issue's artifact folder. Include the source, dependency manifest and lockfile when applicable, and a short run guide. Hand off a reproducible snapshot or bundle through the issue. Move implementation into the product repository only through the normal delivery workflow.

## Handoffs across tools and machines

The issue records the owner, exact artifact revision, and where to retrieve it. A local relative path helps people on the source machine find the editable file. Attach or link a durable snapshot for anyone working elsewhere. For a design review, pair the native file with a viewable export such as PNG or PDF and a short decision record. For a runnable prototype, include the run instructions and state which parts are mocked. Use stable, revisioned names and keep earlier review revisions available.

Use the same structure with a different issue tracker or design tool. Map issue IDs and artifact storage in that integration. Keep machine-specific paths, server configuration, and tool commands in integration documentation. The published artifact and issue record are the handoff across tools.

## Migrating an existing prototype

Identify its owning issue, current revision, generated files, and any running preview before moving it. Preserve tracked history with a Git reference and keep useful evidence in the issue's artifact folder. Stop or move a running preview only when it can be taken offline safely. Update the run instructions and issue's retrieval reference, then retire the old working path once the copy is verified.
