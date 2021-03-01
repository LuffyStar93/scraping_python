const api_url = "http://localhost:4000/jordan"; 


async function getData(url){
    const response = await fetch(url);
    let data = await response.json();
    console.log(data);
    displayData(data);
    return data
    }
getData(api_url)


function displayData(data){
    data.forEach(element => {
        let tbody = document.querySelector('tbody');
        let tr = document.createElement("tr");
        let colonne1 = tr.insertCell(0);
            colonne1.innerHTML += `<img src="${element[1]}"></img>` ;
        let colonne2 = tr.insertCell(1);
	        colonne2.innerHTML += element[2];
        let colonne3 = tr.insertCell(2);
            colonne3.innerHTML += element[3];
        let colonne4 = tr.insertCell(3);
            colonne4.innerHTML += element[4];
        let colonne5 = tr.insertCell(4);
            colonne5.innerHTML += element[5];
        tbody.appendChild(tr);
    });
}