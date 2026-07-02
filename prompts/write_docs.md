# Write Docs

## Goal

To write, update, sync, align, reconcile and maintain docs for the given file, directory or project.

## Workflow

1. **Initiation**: Start by asking the user for the specific file, directory, or component that needs to be documented.
2. **Analysis**: Once the target is provided, parse the target codebase/files, cross-reference with any existing documentation, and determine what is missing, outdated, or needs updating.
3. **Generation**: Automatically generate all four types of documentation (Tutorials, How-To Guides, Reference, Explanation) to ensure a complete set for the target component.

## Docs Structure

The documentation must follow the [Divio documentation structure](https://docs.divio.com/documentation-system/structure/).
The full system is explained here: https://docs.divio.com/documentation-system/

Create dedicated folders for each documentation type within the `docs/` directory and organize files within them:
- `docs/tutorials/`
- `docs/how-to/`
- `docs/reference/`
- `docs/explanation/`

Unless specified otherwise, docs should be written in the project root's `docs/` directory.

In Root there must be a README.md.

## Docs Rules & Style

- **Markdown**: The docs should follow proper markdown syntax from https://spec.commonmark.org/0.31.2/
- **Tone**: Maintain a professional, technical, but accessible tone.
- **Voice**: Use active voice.
- **Examples**: Provide clear, practical examples where applicable.
- **Section Ordering**: In getting-started tutorials and guides, position all CLI command-related sections before any Web UI-related sections to ensure terminal verification succeeds before browser tools are built.

## Feedback

While generating documentation, if you have any doubts, pause and ask the user for clarification before proceeding.
