import '@common/scss/main.scss';
// noinspection ES6UnusedImports
import {Dropdown} from 'bootstrap';

// Ensure locales are made for all languages
// noinspection JSUnusedLocalSymbols
const helloWorld = gettext('Hello World');

window.addEventListener('DOMContentLoaded', () => {
    const scrollMotdBreak = 64;
    const motdElement = document.getElementById('al-motd');
    if (motdElement) {
        const navBarElement = document.getElementById('al-primary-navbar');
        const maybeHideMotd = () => {
            if (window.scrollY > scrollMotdBreak && motdElement.style.display !== 'none') {
                motdElement.style.display = 'none';
                navBarElement.classList.remove('with-motd');
            } else if (window.scrollY <= scrollMotdBreak && motdElement.style.display !== 'block') {
                motdElement.style.display = 'block';
                navBarElement.classList.add('with-motd');
            }
        };

        document.addEventListener('scroll', maybeHideMotd);
        maybeHideMotd()
    }
});
