//"https://httpbin.org/post"
//"https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"

let postData = {
	"dates": [
		"2024-11-11",
		"2024-11-12",
		"2024-11-13",
		"2024-11-14",
		"2024-11-15"
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
			"date": "2024-11-11",
			"type": "0036",
			"clientName": "",
			"clientAddress": ""
		},
		{
			"date": "2024-11-12",
			"type": "0036",
			"clientName": "",
			"clientAddress": ""
		},
		{
			"date": "2024-11-13",
			"type": "0036",
			"clientName": "",
			"clientAddress": ""
		},
		{
			"date": "2024-11-14",
			"type": "0036",
			"clientName": "",
			"clientAddress": ""
		},
		{
			"date": "2024-11-15",
			"type": "0036",
			"clientName": "",
			"clientAddress": ""
		}
	]
};

fetch("https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking", {
  method: 'POST',
  body: JSON.stringify(postData),
  headers: {
   'Content-type': 'application/json; charset=UTF-8'
  }
}).then(res => res.json()).then(console.log);
