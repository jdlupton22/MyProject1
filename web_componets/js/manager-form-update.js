const table = document.getElementById("reimbursementTable");
const tableBody = document.getElementById("reimbursementBody");

async function createReimbursement() {
    const requestId = document.getElementById("requestId").value;
    const projectAward = document.getElementById("projectAward").value;
    const urgent = document.getElementById("urgent").value;
    const status = document.getElementById("status").value;
    const stage = document.getElementById("stage").value;
    const requestDateTime = document.getElementById("requestDateTime").value;
    
    let response = await fetch("http://127.0.0.1:5000/reimbursement", {
        method:"POST",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            "requestId": requestId,
            "projectAward": projectAward,
            "urgent": urgent,
            "status": status,
            "stage": stage,
            "requestDateTime": requestDateTime})
    }
    )
    if (response.status === 200) {
        let body = await response.json();
        alert("Request Submitted Successful!") 
    } else {
        let body = await response.json;
        alert("Request Failed!")
    }
}

async function getMyReimbursementData(){
    let url = "http://127.0.0.1:5000/reimbursement/user";
    let response = await fetch(url);

    if (response.status === 200) {
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the reimbursement information!")
    }
}

function populateData(responseBody) {
    for (let reimbursement of responseBody) {
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.requestId}</td>
                                <td>${reimbursement.projectAward}</td>
                                <td>${reimbursement.urgent}</td>
                                <td>${reimbursement.status}</td>
                                <td>${reimbursement.stage}</td>
                                <td>${reimbursement.requestDateTime}</td>`
        tableBody.appendChild(tableRow)
    }
}

getMyReimbursementData()

function Logout() {
    sessionStorage.clear()
    window.location.href = "login.html";
}