
//"https://httpbin.org/post"
//"https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"

let postData1 = {
  "dates": [
    "2024-11-11"
  ],  
  "facilityId": "6448cee7bf530c0226ea4d4d",
  "positionId": "6448cee7bf530c0226ea4d55",
  "x": 1225,
  "y": 1504,
  "code": "008",
  "parking": [
    {
      "parkingRequested": false,
      "plateNumber": "",
      "type": "All"
    }
  ],
  "datesAndType": [
    {
      "date": "2024-11-11",
      "type": "0036",
      "clientName": "",
      "clientAddress": ""
    }
  ]
}

let postData2 = {
  "dates": [
    "2024-11-12"
  ],
  "facilityId": "6448cee7bf530c0226ea4d4d",
  "positionId": "6448cee7bf530c0226ea4d5c",
  "x": 1404,
  "y": 881,
  "code": "015", 
  "parking": [
    {
      "parkingRequested": false,
      "plateNumber": "",
      "type": "All"
    }
  ],
  "datesAndType": [
    {
      "date": "2024-11-12",
      "type": "0036",
      "clientName": "",
      "clientAddress": ""
    }
  ]
}

let postData3 = {
  "dates": [
    "2024-11-13"
  ],
  "facilityId": "6448d14dbf530c0226ea4d6a",
  "positionId": "6448d14dbf530c0226ea4d72",
  "x": 759.0,
  "y": 1768.0,
  "code": "023",
  "parking": [
    {
      "parkingRequested": false,
      "plateNumber": "",
      "type": "All"
    }
  ],
  "datesAndType": [
    {
      "date": "2024-11-13",
      "type": "0036",
      "clientName": "",
      "clientAddress": ""
    }
  ]
}

let postData4 = {
  "dates": [
    "2024-11-14"
  ],
  "facilityId": "6448cee7bf530c0226ea4d4d",
  "positionId": "6448cee7bf530c0226ea4d57",
  "x": 1349,
  "y": 1238,
  "code": "010",
  "parking": [
    {
      "parkingRequested": false,
      "plateNumber": "",
      "type": "All"
    }
  ],
  "datesAndType": [
    {
      "date": "2024-11-14",
      "type": "0036",
      "clientName": "",
      "clientAddress": ""
    }
  ]
}

let postData5 = {
  "dates": [
    "2024-11-15"
  ],
  "facilityId": "6448d14dbf530c0226ea4d6a",
  "positionId": "6448d14dbf530c0226ea4d88",
  "x": 1247,
  "y": 921,
  "code": "046",
  "parking": [
    {
      "parkingRequested": false,
      "plateNumber": "",
      "type": "All"
    }
  ],
  "datesAndType": [
    {
      "date": "2024-11-15",
      "type": "0036",
      "clientName": "",
      "clientAddress": ""
    }
  ]
}

const payloads = [
  { data: postData1 },
  { data: postData2 },
  { data: postData3 },
  { data: postData4 },
  { data: postData5 }
];


// Function to send a POST request and log the time taken for each
async function sendPostRequest(payload, index) {
  const startTime = Date.now();
  const response = await fetch("https://httpbin.org/post", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
  });
  const data = await response.json();
  const endTime = Date.now();
  console.log(`Request ${index + 1} completed in ${endTime - startTime} ms`);
  return data;
}

// Send all requests concurrently and wait for all to complete
Promise.all(payloads.map((payload, index) => sendPostRequest(payload, index)))
  .then(results => console.log("All responses:", results))
  .catch(error => console.error("Error with requests:", error));

