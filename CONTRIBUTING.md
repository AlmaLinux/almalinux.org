# Contributing

If you are interested in making a contribution there are a few ways you could help out the project.

## Contributing a blog post

We welcome blog posts of almost any kind from our community! We accept content that covers topics that relate to AlmaLinux OS, the AlmaLinux OS Foundation. If you aren't sure if your blog post topic would be a good one, feel free to create an issue on this repo and ask! You can also join our chat and ask in the Marketing room. 

### Process information

- Before you begin writing the blog post, we strongly recommend that you search existing open and closed issues for similar content, to prevent duplication. 
- We also recommend that you open an issue on the repo to propose your blog post before you begin writing it, to ensure that your blog post would be appropriate for the AlmaLinux blog.
- Please fork the almalinux.org repo and submit your blog post from there. 

#### The content of your .md file

Our website is built in Hugo, with some quirks. To add a blog post successfully to the website, take the following steps:

- create a new file in ./content/blog named what you'd like the slug (URL) to be, with a file extension of '.md'. For example, the blog post at almalinux.org/blog/celebrating-500k-docker-pulls is in a file named ./content/blog/celebrating-500k-docker-pulls.md.

- The top of your file should be the metadata for your post. The meta information should be updated to include your posts information. The content is defined and further explained below.

```
---
title: ""
type: blog
author: 
 name: ""
 bio: ""
 image: /users/
date: ''
post:
	title: ""
	image: /blog-images/
---
```

- The **title** is what you'd like displayed at the top of the post.
- The **type** should always be 'blog'.  
- The **name** listed should be yours (either legal name or chosen name or moniker) 
- Your **bio** will be displayed directly under your name, so please keep this to 60 characters or less. 
- Your author **image** should be appropriate for an all-audiences website and added to ./static/users/ in .png format. The file will serve from /users/, so do not change the beginning of this path. 
- The **date** is the date you want to see the blog post published, but we cannot always guarantee a publishing timeline. 
- The post **title** should match the above.
- A post **image** should be included, and will be displayed both on the almalinux.org/blog/ feed, and as the header image on the full-page blog post. Your image should not violate any trademarks or copyrights, and should be relevant to blog content. Once created, a PNG version of your image should be placed in ./static/blog-images/ The file will serve from /blog-images/, so do not change the beginning of this path. 
- Below the --- of the metadata block, you should place the content of your blog post. This content should be in markdown format, and any images you want to include in your post can be added 
- Before submitting your PR, please test that your content loads correctly by building the site locally with the command `hugo server`


### Some notes about content

- define all terms used (especially acronyms) so that all readers may understand your content. 
- content submitted to the AlmaLinux blog should be unique and not posted elsewhere on the internet.
- by submitting content to the AlmaLinux website, you are affirming that you are the sole author of all text and images used in the post, and that you own all rights to publish said content.
- external links are allowed, but links to paywalled websites or obvious use of a blogpost on the AlmaLinux site as an SEO builder for another website is prohibited.

## Filing issues

You are free to use [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues) to submit bugs and for discussions related to the codebase.

### Reporting a Bug

Good bug reports can be very helpful. A bug is a demonstrable problem with the code or functionality.

Please use the [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues) and check if the issue has already been reported.

A good bug report should be as detailed as possible, so that others won't have to follow up for the essential details.

- Submit a bug in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues)

### Requesting a Feature

1. [Search the issues](https://github.com/AlmaLinux/almalinux.org/issues) for any open requests for the same feature, and give a thumbs up or +1 on existing requests.
1. If no previous requests exist, create a new issue. Please be as clear as possible about why the feature is needed and the intended use case.

- Request a feature in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues)

## Contributing code

If you plan to propose code changes, a corresponding issue must be created. If you are not contributing code to fix an existing issue, you should first create an [issue](https://github.com/AlmaLinux/almalinux.org/issues) with a brief proposal in order to discuss it with the project contributors first.

This is necessary to avoid more than one contributor working on the same feature/change and to avoid someone from spending time on feature/change that would not be merged for any reason.

For smaller contributions use this workflow:

* Create an [issue](https://github.com/AlmaLinux/almalinux.org/issues) describing the changes.
* Await confirmation from contributors.
* Fork the project.
* Create a branch for your feature or bug fix.
* Add code changes, relevant documentation, etc.
* Send a pull request.  All PRs should be made against the `master` branch.  A dev site will be automatically created based on the PR.  Localization will not be fully working as this pipeline does not run the localization scripts.

After one of the contributors has checked and approved the changes, they will be merged into master branch and will be included in the next deployment.

## Approval of changes

Before any changes can be merged:

- All minor or cosmetic changes (typos, minor styling, etc) can be approved and merged by any contributor with master merge rights
- All non-cosmetic changes to the website requires the approval of the Marketing lead
- All major changes that are not purely technical, and fundamental changes in technology requires the approval of the AlmaLinux OS Community Manager.
