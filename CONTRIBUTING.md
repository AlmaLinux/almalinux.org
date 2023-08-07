# Contributing

If you are interested in making a contribution there are a few ways you could help out the project.

## Filing issues

You are free to use [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues) to submit bugs and for
discussions related to the codebase.

### Reporting a Bug

Good bug reports can be very helpful. A bug is a demonstrable problem with the code or functionality.

Please use the [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues) and check if the issue has
already been reported.

A good bug report should be as detailed as possible, so that others won't have to follow up for the essential details.

- Submit a bug in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues)

### Requesting a Feature

1. [Search the issues](https://github.com/AlmaLinux/almalinux.org/issues) for any previous requests for the same
   feature, and give a thumbs up or +1 on existing requests.
1. If no previous requests exist, create a new issue. Please be as clear as possible about why the feature is needed and
   the intended use case.

- Request a feature in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues)

## Contributing code

If you plan to propose code changes it is required you create
an [issue](https://github.com/AlmaLinux/almalinux.org/issues) with a brief proposal and discuss it with us first.

This is necessary to avoid more than one contributor working on the same feature/change and to avoid someone from
spending time on feature/change that would not be merged for any reason.

For smaller contributions use this workflow:

* Create an [issue](https://github.com/AlmaLinux/almalinux.org/issues) describing the changes.
* Await confirmation from contributors.
* Fork the project.
* Create a branch for your feature or bug fix.
* Add code changes, relevant documentation, etc.
* Send a pull request.  All PRs should be made against the `master` branch.  A dev site will be automatically created
  based on the PR.  Localization will not be fully working as this pipeline does not run the localization scripts.

After one of the contributors has checked and approved the changes, they will be merged into master branch and will be
included in the next deployment.

### Styling Guide

Please adhere to the styling guidelines listed below when contributing to the codebase.

## Code/Syntax Highlighting

Code/Syntax highlighting is achieved by the builtin [Hugo syntax highlighting](https://gohugo.io/content-management/syntax-highlighting/) feature, which utilizes [Chroma](https://github.com/alecthomas/chroma).

While Hugo supports two syntaxes, we use traditional code fencing for code samples:

````plaintext
```go
package main

import "fmt"

func main () {
    fmt.Println("This line is printed")
}
```
````

Supported highlighting languages can be found [here](https://gohugo.io/content-management/syntax-highlighting/#list-of-chroma-highlighting-languages).

## Approval of changes

Before any changes can be merged:

- All minor or cosmetic changes (typos, minor styling, etc) can be approved and merged by any contributor with master
  merge rights,
- All non-cosmetic changes to the website requires the approval of the Web Team lead and at least one other Web Team
  member.
- All major changes that are not purely technical, and fundamental changes in technology requires the approval of the
  AlmaLinux OS Community Manager.
