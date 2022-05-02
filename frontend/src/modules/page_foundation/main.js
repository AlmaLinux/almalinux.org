import './main.scss';

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('contributor').addEventListener('click',function ()
        {
            const contrib = document.getElementById('al-contributor-info');
            const mirr = document.getElementById('al-mirror-info');
            const spons = document.getElementById('al-sponsor-info');
            mirr.style.display = 'none';
            spons.style.display = 'none';
            if (contrib.style.display === 'none' | contrib.style.display == '') {
                contrib.style.display = 'block';
            } else {
                contrib.style.display = 'none';
            }
        }
    );

    document.getElementById('mirror').addEventListener('click',function ()
        {
            const mirr = document.getElementById('al-mirror-info');
            const contrib = document.getElementById('al-contributor-info');
            const spons = document.getElementById('al-sponsor-info');
            contrib.style.display = 'none';
            spons.style.display = 'none';
            if (mirr.style.display === 'none'  | mirr.style.display == '') {
                mirr.style.display = 'block';
            } else {
                mirr.style.display = 'none'; 
            }
        }
    );

    document.getElementById('sponsor').addEventListener('click',function ()
        {
            const spons = document.getElementById('al-sponsor-info');
            const mirr = document.getElementById('al-mirror-info');
            const contrib = document.getElementById('al-contributor-info');
            contrib.style.display = 'none';
            mirr.style.display = 'none';
            if (spons.style.display === 'none' | spons.style.display == '') {
                spons.style.display = 'block';
            } else {
                spons.style.display = 'none';
            }
        }
    );
});