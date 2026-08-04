# Agile Workflows & Kanban

## Research & Learn

**How does a Kanban board work, and how does it help manage workflow?**

A Kanban board represents work as cards moving left to right across columns, where each column is a stage in the workflow. Instead of tracking tasks from memory or a scattered list, the board gives a single, real-time view of what's queued, what's actively being worked on, and what's stuck, which is useful both for the person doing the work and anyone reviewing it. Because cards only move forward through defined stages, bottlenecks (for example ten cards piled up waiting on review) become visible immediately instead of staying hidden. Unlike Scrum, Kanban isn't built around fixed-length sprints, work flows continuously and priorities can shift at any time, as long as the WIP limits described below are respected.

**What do the different columns on a Kanban board represent?**

Backlog holds tasks that have been identified but not yet prioritised, the full pool of future work. Not Started (or To Do) is for tasks that have been prioritised and are ready to be picked up next. In Progress is for tasks someone is actively working on right now. Blocked is for tasks that can't move forward because they're waiting on something, a decision, another task, or external input. Ready for Review is for work believed to be complete and waiting on someone (or something, like an automated bot check) to verify it. Approved/Done is for work that's been reviewed and is genuinely finished. The exact names vary by team, but each column is a checkpoint that shows how close a task actually is to being done, rather than just whether someone has touched it.

**How do tasks move through the board, and who is responsible for updating them?**

A card moves from Backlog to Not Started once it's prioritised, to In Progress once someone starts it, and then either to Blocked if it gets stuck or to Ready for Review once the work is believed complete, before finally landing in Approved/Done. Responsibility for moving a card sits with whoever owns that stage: the person doing the task moves it into In Progress and later into Blocked or Ready for Review, while a reviewer (a teammate, or an automated bot running checks) moves it from Ready for Review into Approved, or back into In Progress if changes are needed. The board is only useful if it reflects reality, so updating a card's status promptly is part of the task itself, not something to do later.

**What are the benefits of limiting work in progress (WIP)?**

Limiting WIP reduces multitasking and context-switching, working on fewer things at once means each task actually gets finished instead of several sitting half-done simultaneously. It surfaces bottlenecks early, hitting a WIP limit forces existing blockers to be resolved before new work starts, rather than letting unfinished tasks quietly pile up. It also improves predictability, since a more even flow of work makes it easier to estimate how long new tasks will take, and it encourages collaboration, because someone who can't start new work due to a WIP limit is incentivised to help unblock or review what's already in progress instead.

## Reflection

**How does Kanban help manage priorities and avoid overload?**

Before working with a board explicitly, tasks tended to exist only as a mental list, which made it hard to tell what was genuinely urgent versus what just felt urgent because it was most recent. Putting every task on the board as a card forces prioritisation to be a visible, deliberate decision, I have to actually decide what moves into Not Started next rather than reacting to whatever surfaced last. The WIP limit is what actually prevents overload though: capping how many cards can sit In Progress at once means I have to finish or consciously park existing work before starting something new, which keeps effort concentrated instead of spread thin across too many half-finished tasks.

**How can you improve your workflow using Kanban principles?**

Keeping the Blocked column honest is the biggest one, letting a stuck task quietly sit in In Progress instead of moving it to Blocked hides the actual obstacle instead of surfacing it for resolution. Setting a personal WIP limit, even working solo, helps too, capping it at one or two cards in progress at a time pushes back against the urge to open several tasks and finish none of them properly. Reviewing the board daily rather than only when starting new work also matters, so cards sitting in Ready for Review or Blocked don't quietly stagnate. Finally, breaking large tasks into smaller cards helps: a card that stays In Progress for a long time is usually a sign it should have been split, since smaller cards make both progress and blockers easier to see.

## Task

**Board created:** a GitHub Projects (Kanban) board was added to this repo with the columns Not Started, In Progress, Blocked, Ready for Review, and Approved, matching the workflow described above.

**Task moved through the process:** the Agile Workflows & Kanban issue itself (this task) was moved across the board from Not Started, to In Progress while researching and writing this reflection, to Ready for Review once the file was drafted, and finally to Approved once complete, updating its status at each stage.

**One way to improve task tracking in my role:** explicitly use the Blocked status whenever a task is waiting on something external (a review, a decision, or a dependency) instead of leaving it sitting in In Progress. That keeps the board an accurate signal of what genuinely needs attention versus what's just pending someone else, rather than making every stalled task look identical to active work.
