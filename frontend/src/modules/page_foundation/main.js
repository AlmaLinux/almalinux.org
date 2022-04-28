import './main.scss';
document.getElementById("contributor").addEventListener('click',function ()
    {
        var cont = document.getElementById("al-contributor-info");
        var mirr = document.getElementById("al-mirror-info");
        var spons = document.getElementById("al-sponsor-info");
        mirr.style.display = "none"
        spons.style.display = "none"
        if (cont.style.display === "none" | cont.style.display == "") {
            cont.style.display = "block";
        } else {
            console.log("else")
            cont.style.display = "none";
        }
    }
);

document.getElementById("mirror").addEventListener('click',function ()
    {
        var mirr = document.getElementById("al-mirror-info");
        var cont = document.getElementById("al-contributor-info");
        var spons = document.getElementById("al-sponsor-info");
        cont.style.display = "none"
        spons.style.display = "none"
        if (mirr.style.display === "none"  | mirr.style.display == "") {
            mirr.style.display = "block";
        } else {
            mirr.style.display = "none"; 
        }
    }
);

document.getElementById("sponsor").addEventListener('click',function ()
    {
        var spons = document.getElementById("al-sponsor-info");
        var mirr = document.getElementById("al-mirror-info");
        var cont = document.getElementById("al-contributor-info");
        cont.style.display = "none"
        mirr.style.display = "none"
        if (spons.style.display === "none" | mirr.style.display == "") {
            spons.style.display = "block";
        } else {
            spons.style.display = "none";
        }
    }
);