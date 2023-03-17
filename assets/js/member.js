"use strict";
(self.webpackChunk = self.webpackChunk || []).push([
    [229],
    {
        63: function () {
            window.addEventListener("DOMContentLoaded", function () {
                document.getElementById("contributor").addEventListener("click", function () {
                    var e = document.getElementById("al-contributor-info"),
                        n = document.getElementById("al-mirror-info"),
                        t = document.getElementById("al-sponsor-info");
                    (n.style.display = "none"), (t.style.display = "none"), ("none" === e.style.display) | ("" == e.style.display) ? (e.style.display = "block") : (e.style.display = "none");
                }),
                    document.getElementById("mirror").addEventListener("click", function () {
                        var e = document.getElementById("al-mirror-info"),
                            n = document.getElementById("al-contributor-info"),
                            t = document.getElementById("al-sponsor-info");
                        (n.style.display = "none"), (t.style.display = "none"), ("none" === e.style.display) | ("" == e.style.display) ? (e.style.display = "block") : (e.style.display = "none");
                    }),

                    document.getElementById("sponsor").addEventListener("click", function () {
                        var e = document.getElementById("al-sponsor-info"),
                            n = document.getElementById("al-mirror-info");
                        (document.getElementById("al-contributor-info").style.display = "none"), (n.style.display = "none"), ("none" === e.style.display) | ("" == e.style.display) ? (e.style.display = "block") : (e.style.display = "none");
                    });
            });
        },
    },
    function (e) {
        var n;
        (n = 63), e((e.s = n));
    },
]);
