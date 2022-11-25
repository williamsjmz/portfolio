document.addEventListener('DOMContentLoaded', () => {

    fetchProjects();

});



function fetchProjects() {

    fetch(`get/all/`, {

        method: 'GET',

    })
        .then(response => response.json())
        .then(data => {

            if (data.status == 200) {

                if (data.alert) {

                    insertAlert(data.alert, "projects-container", "warning");

                } else {

                    Object.keys(data).forEach(key => {

                        if (key != "status") {

                            insertProject(data[key]);

                        }

                    })

                }

                Object.keys(data).forEach(key => {


    
                });
                
            } else if (data.status == 405) {

                insertAlert(data["error"],  "projects-container", "danger");

            } else if (data.status == 500) {

                insertAlert(data["error"],  "projects-container", "danger");

            }  else {

                insertAlert("Ocurrió un error inesperado, intentalo de nuevo.",  "projects-container", "warning");

            }

        });

}



function insertProject(project) {

    const $container = document.getElementById('projects-container');
    
    const $outterDiv = document.createElement('div');
    $outterDiv.setAttribute('class', 'col-md-6 col-lg-4');

    const $innerDiv = document.createElement('div');
    $innerDiv.setAttribute('class', 'project-card-no-image');

    const $divContainer = document.createElement('div');
    $innerDiv.setAttribute('style', 'margin-bottom: 20px;');

    const $h3 = document.createElement('h3');
    $h3.setAttribute('class', 'h3-name');
    $h3.innerText = `${project['name']}`;

    const $pPrjojectType = document.createElement('p');
    $pPrjojectType.setAttribute('style', 'margin-bottom: 5px;display: block;font-size: 12px;color: rgb(130,135,139);');
    $pPrjojectType.innerText = `${project['project_type']}`;

    const $h4 = document.createElement('h4');
    $h4.innerText = `${project['description']}`;

    const $divButtonsContainer = document.createElement('div');
    $divButtonsContainer.setAttribute('style', 'display: block');

    const $repositoryButton = document.createElement('a');
    $repositoryButton.setAttribute('class', 'btn btn-outline-primary btn-sm');
    $repositoryButton.setAttribute('role', 'button');
    $repositoryButton.setAttribute('href', `${project['repository']}`);
    $repositoryButton.setAttribute('target', '_blank');
    $repositoryButton.innerText = 'Repository';

    const $siteButton = document.createElement('a');
    $siteButton.setAttribute('class', 'btn btn-outline-primary btn-sm');
    $siteButton.setAttribute('role', 'button');
    $siteButton.setAttribute('href', `${project['site']}`);
    $siteButton.setAttribute('target', '_blank');
    $siteButton.setAttribute('style', 'margin-left: 10px;');
    $siteButton.innerText = 'Site';

    const $div = document.createElement('div');
    $div.setAttribute('class', 'tags');
    $div.setAttribute('style', 'display: block;');

    const $pTechnology = document.createElement('p');
    $pTechnology.setAttribute('style', 'display: block;font-size: 12px;color: rgb(130,135,139);');
    
    let newInnerText = 'Technologies:&nbsp;&nbsp;';

    project['technologies'].forEach(technology => {

        newInnerText = newInnerText + technology.name + "&nbsp;&nbsp;&nbsp;";

    });

    $pTechnology.innerHTML = newInnerText;

    $divContainer.appendChild($h3);
    $divContainer.appendChild($pPrjojectType);
    $divContainer.appendChild($pTechnology);

    $divButtonsContainer.appendChild($repositoryButton);
    if ($siteButton.getAttribute('href') != '') {
        $divButtonsContainer.appendChild($siteButton);
    }
    

    $innerDiv.appendChild($divContainer);
    $innerDiv.appendChild($div);
    $innerDiv.appendChild($h4);
    $innerDiv.appendChild($divButtonsContainer);
    

    $outterDiv.appendChild($innerDiv);

    $container.appendChild($outterDiv);

}



function insertAlert(error, containerID, alertType) {

    const $div = document.createElement("div");

    $div.setAttribute("class", `alert alert-${alertType}`);
    $div.innerText = `${error}`;

    document.getElementById(`${containerID}`).appendChild($div);

}