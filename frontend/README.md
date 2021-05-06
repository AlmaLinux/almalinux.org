# almalinux.org JavaScript and SCSS modules

This source module contains frontend specific source code for almalinux.org.

- NodeJS v15.
- Yarn for dependency management.
- Modern JavaScript.
- SCSS for stylesheets.

## Source structure

All CSS/JS code can be found in `src/` directory.

### `src/common`

Common entry point is used for JavaScript and SCSS code that is expected to be used by all or most of the website pages,
and for otherwise reusable code.

### `src/modules`

Modules root directory contains modular JS/SCSS for features isolate to some specific domain, such as a specific feature
or page. Features should be generally organized following this convention:

```
src/modules/feature_<NAME>
src/modules/page_<NAME>
```

The difference between `page_*` and `feature_*` is that page specific code is limited to be used within a single view,
while features should be reusable.

Each module should contain a README.md file to document features, use and dependencies for said specific code module.

`<NAME>` identifiers should be short, but descriptive, and should follow pattern `[a-z_]+`.

#### Dependencies within modules

- `page_*` is allowed to have zero or more dependencies on `feature_*` modules, or code in `src/common`
- `page_*` must not depend on code in another `_page*`
- `feature_*` can depend on another `feature_*`.

