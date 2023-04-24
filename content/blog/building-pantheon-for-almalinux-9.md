---
title: "Building Pantheon Desktop Environment"
type: blog
author: 
 name: "Sofia Boldyreva"
 bio: "Technical Writer for AlmaLinux OS Project"
 image: /users/sofia-boldyreva.png
date: '2023-04-20'
post:
    title: "Building Pantheon Desktop Environment"
    image: /blog-images/welcome-to-almalinux-9-pantheon.png

---

# Building Pantheon Desktop Environment 

Hello, AlmaLinux Community! 
Let me start off by introducing myself - my name is Sonia, and I'm a Technical Writer for AlmaLinux OS Project. In this blog post, I'm describing one of the ways that I have contributed to AlmaLinux recently. With much learning, I have successfully ported the Pantheon desktop environment to AlmaLinux 9.

## The Idea 

Several key factors contributed to the successful integration of AlmaLinux with the Pantheon desktop environment:
1. The desire to broaden and diversify the spectrum of AlmaLinux Desktop Environments variants.
2. The aesthetic appeal of the Pantheon desktop environment, which I found to be quite visually pleasing.
3. As a newcomer to this technical domain, the project offered a unique opportunity to expand my knowledge and skillset.
4. The entire process was an enjoyable and engaging experience.

These reasons provided a solid foundation for embarking on the AlmaLinux Pantheon project.
My journey demonstrates that contributing to open-source projects is achievable at any stage without requiring extensive expertise in Linux or programming.

Now, it’s time to delve into the various stages of the development process.

## Preparations and Requirements 

### Researching the Pantheon Desktop Environment 

I installed the EPEL repo on my Fedora machine, and then installed the Pantheon desktop environment to take a peek at what the packages included. During this phase also I compared a list of [Fedora Pantheon SIG](https://fedoraproject.org/wiki/SIGs/Pantheon) packages that I found on the Internet with what I saw having been installed. 
As I used this install as inspiration, I was mostly focused on rebuilding the Fedora 36 packages. 

The next stage was to rebuild those packages for AlmaLinux. 

### Requirements for rebuilding

* AlmaLinux 9 machine - as I started my experiment with rebuilding the packages locally, I didn't need much. A bare AlmaLinux 9 machine was enough. 
* Installed git - using the `dnf install git-all`.
* `mock` tool - I followed the [AlmaLinux Building Packages Guide](https://wiki.almalinux.org/documentation/building-packages-guide.html) to install `mock` and use it.

### Enabling repositories

Basic research of required Pantheon packages and rebuilding them locally defined that I needed a few extra repositories to be enabled. These repositories may contain some auxiliary packages that might be needed since I don't want to build packages that AlmaLinux already has. 

The enabling commands were taken from the [AlmaLinux Wiki Repositories page](https://wiki.almalinux.org/repos/) unless otherwise noted.


* **EPEL** repo 
* **PowerTools (CRB)** repo
* **Devel** repo
    * I didn't enable this repo server-wide with the `dnf config-manager --set-enabled` command. Devel repo is more like an internal repo and it's not supposed to be enabled on a regular basis. Instead, I enabled it in the **mock** configuration, as you will see below. To do this I made some changes in the AlmaLinux template in `/etc/mock/templates` to set up the devel repository as enabled. 

#### Creating my local repository 

I needed to install some additional tools before building my packages. That's where creating and using a local repo helped me. 

I started by following these instructions, that should work for most Red Hat-based systems:
* **Install the createrepo tool** - Note: this was already installed in my environment when I installed `mock`:
  ```
  dnf install createrepo_c
  ```

* **Create your new repository directory**:
  ```
  mkdir -p /path/to/repository
  ```

* **Copy needed rpms to this directory**. In my case, I didn't have any rpms built yet to copy. Instead, I was just using the `--resultid /path/to/repo` argument in the `mock` command to build the packages directly to the local repo folder. 

* **Run createrepo_с command**:
  ```
  createrepo_c /path/to/repository
  ```

* Each time there's a new package in your local repo folder, run the following command to update the repo:
  ```
  createrepo_c .
  ```

* Now there's an important detail. As opposed to the random internet instruction, I didn't create my repo's config in the `/etc/yum.repos.d` directory. This didn't really work for my purposes. Instead, I followed the advice of Andrew, our Build SIG leader, here and created a new version of the mock config in `/etc/mock/` with the necessary modifications: 
  ```
  include('almalinux-9-x86_64.cfg')
  include('templates/epel-9.tpl')

  # in this block you can see my changes 
  config_opts['yum.conf'] += """
  [el]
  name=el
  baseurl=file:///path/to/repo
  enabled=1
  gpgcheck=0
  """
 
  config_opts['root'] = "alma+epel-9-{{ target_arch }}-local"
  config_opts['description'] = 'AlmaLinux 9 + EPEL'
  ```

## Rebuilding packages 

Of course, I faced a number of issues while building packages with the `mock` tool. Some of the packages demanded changes in spec files - for example, to put changes to match AlmaLinux packages versions. And for some packages, I had to build other versions. But I tried to note the changes that were required below. 


| Package |  Comment| 
| --- | --- |
| [elementary-calculator](https://git.almalinux.org/rpms/elementary-calculator) | | 
| [elementary-calendar](https://git.almalinux.org/rpms/elementary-calendar) | |
| [elementary-camera](https://git.almalinux.org/rpms/elementary-camera) | |
| [elementary-capnet-assist](https://git.almalinux.org/rpms/elementary-capnet-assist) | |
| [elementary-code](https://git.almalinux.org/rpms/elementary-code) | elementary-code spec changes: Replaced libvala required version to 0.48 to match AlmaLinux 9 repositories|
| [elementary-files](https://git.almalinux.org/rpms/elementary-files) | |
| [elementary-greeter](https://git.almalinux.org/rpms/elementary-greeter) | elementary-greeter spec changes: replaced required mutter-clutter, mutter-cogl-pango, mutter-cogl from 10 to 8 to match AlmaLinux 9 repos |
| [elementary-icon-theme](https://git.almalinux.org/rpms/elementary-icon-theme) | |
| [elementary-music](https://git.almalinux.org/rpms/elementary-music) | |
| [elementary-onboarding](https://git.almalinux.org/rpms/elementary-onboarding) | |
| [elementary-photos](https://git.almalinux.org/rpms/elementary-photos) | |
| [elementary-print](https://git.almalinux.org/rpms/elementary-print) | |
| [elementary-screenshot-tool](https://git.almalinux.org/rpms/elementary-screenshot-tool) | |	
| [elementary-shortcut-overlay](https://git.almalinux.org/rpms/elementary-shortcut-overlay) | |
| [elementary-sound-theme](https://git.almalinux.org/rpms/elementary-sound-theme) | |
| [elementary-tasks](https://git.almalinux.org/rpms/elementary-tasks) | |
| [elementary-terminal](https://git.almalinux.org/rpms/elementary-terminal) | |
| [elementary-theme](https://git.almalinux.org/rpms/elementary-theme) | |
| [elementary-videos](https://git.almalinux.org/rpms/elementary-videos) | |
| [elementary-wallpapers](https://git.almalinux.org/rpms/elementary-wallpapers) | |
| [gala](https://git.almalinux.org/rpms/gala) | gala spec changes: elementary-greeter spec changes: replaced required mutter-clutter, mutter-cogl-pango, mutter-cogl from 10 to 8 to match AlmaLinux 9 repos |
| [granite](https://git.almalinux.org/rpms/granite) | |
| [folks](https://git.almalinux.org/rpms/folks) | |
| [telepathy-glib](https://git.almalinux.org/rpms/telepathy-glib) | |
| [telepathy-filesystem](https://git.almalinux.org/rpms/telepathy-filesystem) | |
| [python-dbusmock](https://git.almalinux.org/rpms/python-dbusmock) | |
| [bamf](https://git.almalinux.org/rpms/bamf) | |
| [xcursorgen](https://git.almalinux.org/rpms/xcursorgen) | |
| [libgda](https://git.almalinux.org/rpms/libgda) | |
| [libchamplain](https://git.almalinux.org/rpms/libchamplain) | |
| [vala](https://git.almalinux.org/rpms/vala) | |
| [libgpod](https://git.almalinux.org/rpms/libgpod) | |
| [zeitgeist](https://git.almalinux.org/rpms/zeitgeist) | | 
| [dee](https://git.almalinux.org/rpms/dee) | | 
| [goocanvas2](https://git.almalinux.org/rpms/goocanvas2) | | 
| [rarian](https://git.almalinux.org/rpms/rarian) | |
| [mdbtools](https://git.almalinux.org/rpms/mdbtools) | |
| [impallari-raleway-fonts](https://git.almalinux.org/rpms/impallari-raleway-fonts) | |	
| [pantheon-agent-geoclue2](https://git.almalinux.org/rpms/pantheon-agent-geoclue2) | |
| [pantheon-agent-polkit](https://git.almalinux.org/rpms/pantheon-agent-polkit) | |
| [pantheon-session-settings](https://git.almalinux.org/rpms/pantheon-session-settings) | |
| [plank](https://git.almalinux.org/rpms/plank) | plank spec changes:{{< linebreak >}} - remove BuildRequires: libbamf3{{< linebreak >}} - add BuildRequires: bamf-devel{{< linebreak >}} - add Requires: bamf |
| [switchboard](https://git.almalinux.org/rpms/switchboard) | |
| [switchboard-plug-a11y](https://git.almalinux.org/rpms/switchboard-plug-a11y) | |	
| [switchboard-plug-about](https://git.almalinux.org/rpms/switchboard-plug-about) | |
| [switchboard-plug-applications](https://git.almalinux.org/rpms/switchboard-plug-applications) | |
| [switchboard-plug-bluetooth](https://git.almalinux.org/rpms/switchboard-plug-bluetooth) | |
| [switchboard-plug-display](https://git.almalinux.org/rpms/switchboard-plug-display) | |
| [switchboard-plug-keyboard](https://git.almalinux.org/rpms/switchboard-plug-keyboard) | |
| [switchboard-plug-mouse-touchpad](https://git.almalinux.org/rpms/switchboard-plug-mouse-touchpad) | |
| [switchboard-plug-networking](https://git.almalinux.org/rpms/switchboard-plug-networking) | |
| [switchboard-plug-notifications](https://git.almalinux.org/rpms/switchboard-plug-notifications) | |
| [switchboard-plug-onlineaccounts](https://git.almalinux.org/rpms/switchboard-plug-onlineaccounts) | |
|[ switchboard-plug-pantheon-shell](https://git.almalinux.org/rpms/switchboard-plug-pantheon-shell) | |
| [switchboard-plug-printers](https://git.almalinux.org/rpms/switchboard-plug-printers) | |
| [switchboard-plug-sharing](https://git.almalinux.org/rpms/switchboard-plug-sharing) | |
| [rygel](https://git.almalinux.org/rpms/rygel) | |
| [gst-editing-services](https://git.almalinux.org/rpms/gst-editing-services) | |
| [gupnp-av](https://git.almalinux.org/rpms/gupnp-av) | |
| [gupnp-dlna](https://git.almalinux.org/rpms/gupnp-dlna) | |
| [switchboard-plug-sound](https://git.almalinux.org/rpms/switchboard-plug-sound) | |
| [switchboard-plug-tweaks](https://git.almalinux.org/rpms/switchboard-plug-tweaks) | |
| [wingpanel](https://git.almalinux.org/rpms/wingpanel) | wingpanel spec changes: elementary-greeter spec changes: replaced required mutter-clutter, mutter-cogl-pango, mutter-cogl from 10 to 8 to match AlmaLinux 9 repos |
| [wingpanel-applications-menu](https://git.almalinux.org/rpms/wingpanel-applications-menu) | |	
| [wingpanel-indicator-bluetooth](https://git.almalinux.org/rpms/wingpanel-indicator-bluetooth) | |
| [wingpanel-indicator-datetime](https://git.almalinux.org/rpms/wingpanel-indicator-datetime) | |
| [wingpanel-indicator-keyboard](https://git.almalinux.org/rpms/wingpanel-indicator-keyboard) | |
| [wingpanel-indicator-network](https://git.almalinux.org/rpms/wingpanel-indicator-network) | |
| [wingpanel-indicator-nightlight](https://git.almalinux.org/rpms/wingpanel-indicator-nightlight) | |
| [wingpanel-indicator-notifications](https://git.almalinux.org/rpms/wingpanel-indicator-notifications) | |
|[ wingpanel-indicator-power](https://git.almalinux.org/rpms/wingpanel-indicator-power) | |
|[ wingpanel-indicator-session](https://git.almalinux.org/rpms/wingpanel-indicator-session) | |
| [wingpanel-indicator-sound](https://git.almalinux.org/rpms/wingpanel-indicator-sound) | |
| [elementary-mail](https://git.almalinux.org/rpms/elementary-mail) | |
| [elementary-notifications](https://git.almalinux.org/rpms/elementary-notifications) | |
| [elementary-planner](https://git.almalinux.org/rpms/elementary-planner) | |
| [elementary-settings-daemon](https://git.almalinux.org/rpms/elementary-settings-daemon) | |
| [elementary-sideload](https://git.almalinux.org/rpms/elementary-sideload) | |
| [elementary-xfce-icon-theme](https://git.almalinux.org/rpms/elementary-xfce-icon-theme) | |
| [libxcvt](https://git.almalinux.org/rpms/libxcvt) | |
| [libglib-testing](https://git.almalinux.org/rpms/libglib-testing) | |
| [libadwaita](https://git.almalinux.org/rpms/libadwaita) | |
| [malcontent](https://git.almalinux.org/rpms/malcontent) | |

When I had all the necessary packages built and installed, I could enjoy the new look of AlmaLinux! 

![AlmaLinux-9-Pantheon](/blog-images/almalinux-9-pantheon.png)

Now that I ensured that it actually does work with AlmaLinux, it was time to proceed with the next step - build these packages with [AlmaLinux Build System](https://build.almalinux.org/).

### Uploading sources to AlmaLinux Git Service

I was guided to add all the package sources directly to the [AlmaLinux Git Service](https://git.almalinux.org/). 

#### Getting the AlmaLinux Git Service Utility 

The AlmaLinux Git Service Utility is a tool that is being used to house AlmaLinux package sources.

I followed these [simple instructions](https://git.almalinux.org/almalinux/almalinux-git-utils) on how to use the AlmaLinux Git Service Utility to upload sources. 

* Clone the repository https://git.almalinux.org/almalinux/almalinux-git-utils
* Switch to the repository's directory and install the utility:
  ```python3 setup.py install```
* I used the **alma_blob_upload** utility script to upload the sources. 
  
  **Note:** Run `alma_blob_upload -h` or check the **[instruction](https://git.almalinux.org/almalinux/almalinux-git-utils)** to learn how to use the script.
* [Install](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) AWS-CLI and [add credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

  **Note:** Using the AWS-CLI utility requires having AWS credentials (which were kindly provided to me by Elkhan Mammadli, AlmaLinux Cloud SIG leader)

Now everything is ready to upload the sources. 
* Navigate the browser to https://git.almalinux.org/.
* Login using the GitHub account. 
* Upload your sources - I was granted the "AlmaLinux Team member" access so I was able to upload my sources as AlmaLinux sources.
* Create a new repository - the repository's name is after the .spec file. This is also the project's name.

Back on your AlmaLinux computer
* Clone the empty repository that you just created and switch to its directory.
* Create a *.gitignore* file 
  ``` 
  touch .gitignore
  ```
* Create SPECS and SOURCES folders in the project's directory. 
  ```
   mkdir SPECS 
   mkdir SOURCES
  ```
* Switch to the */project-name/SOURCES* directory and place the *.src.rpm* file there - I used source rpms that I got as a result of rebuilding the package locally. 
* Run the following command to extract contents:
  ```
  rpm2cpio %src.rpm_file_name | cpio -i 
  ```
* You can then delete *.src.rpm* file. 
* Move *.spec* file to the */project-name/SPECS* directory. 
* Switch to the project's directory and add the extracted `.tar` archive file to the *.gitignore* file like this:
  ```
  SOURCES/archive_file_name
  ```
* Upload the source using the alma_blob_upload script:
  ```
  alma_blob_upload -f SOURCES/archive_file_name -o .project_name.metadata
  ```
* Add the files for the commit:
  ```
  git add * .gitignore .project_name.metadata
  ```
* Send the commit and push the changes.
  ```
   git push
  ```
* Go back to the repository in the browser to check that everything's uploaded and in place. I also renamed the branch name to include *a9* in Settings to make it more clear that this package was for AlmaLinux OS 9.

### Revamping Packages with AlmaLinux Build System
Once the source is uploaded, the AlmaLinux Build System can be utilized to build the package. I adhered to the guidelines for creating my own [community repository](https://github.com/AlmaLinux/build-system/wiki/AlmaLinux-Build-System-Guide-for-Authorised-Users#product-feed), [initiating new builds](https://github.com/AlmaLinux/build-system/wiki/AlmaLinux-Build-System-Guide-for-Authorised-Users#new-build) using the “add a project from git.almalinux.org” option, and incorporating the build into the community repository.

The [AlmaLinux-Pantheon Community Repository](https://build.almalinux.org/product/31) can be installed to access the AlmaLinux 9 required packages for all 4 supported architectures. 

## Installing Pantheon

To install Pantheon desktop packages you need to enable a few additional repos:
* PowerTools/CRB and EPEL - check the [wiki](https://wiki.almalinux.org/repos/) for commands.
* Community repo
    * Install core dnf plugins that contains COPR plugin
    ```
      dnf install dnf-plugins-core
    ```
    * Download AlmaLinux configuration file in your system
    ```
      curl -o /etc/dnf/plugins/copr.d/almalinux.conf \
      https://raw.githubusercontent.com/AlmaLinux/albs-web-server/master/reference_data/almalinux.conf
    ```
    * Enable Pantheon community repo
    ```
      dnf copr --hub build.almalinux.org enable sboldyreva/Pantheon-group
    ```

* Now simply run the following command to install packages and enjoy the new desktop environment:
  ```
  dnf group install "Pantheon Desktop" 
  ```

## Wrapping Up with Enthusiasm: Test, Contribute, and Collaborate!
As we conclude, I’m thrilled to invite you all to test and explore the fresh new look of AlmaLinux! Join the conversation in the [Mattermost chat](https://chat.almalinux.org/), share your feedback, and let’s work together to refine and enhance this exciting desktop experience. Let’s make it even better together! 

## Acknowledgments

It’s important to me that I also note that I was not alone in this endeavor - I received invaluable support from AlmaLinux engineers, Andrew Lukoshko and Eduard Abdullin.
Also, a thank you to the AlmaLinux Evangelist, Pawel Suchanecki, whose assistance helped me to create this article.


