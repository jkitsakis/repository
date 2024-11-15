from string import Template


class Parameters:

    date_strings = ['{2024-11-18}', '{2024-11-19}', '{2024-11-20}', '{2024-11-21}', '{2024-11-22}']

    planner_url = "https://myplanner.netcompany-intrasoft.com"

    available_seats_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/facility/facilities/available/map"

    my_booked_desks_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/future?page=0&size=15"

    book_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"

    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=0CBC02C4AC845EF525F3C49A21115865; TS010ee64b=01eb1053a06986da9e0e299f176fb51d0d3fc4fad35e9ab976fed1310a7ecf37f62d83669e83d769e5d5f394a4c0dd80c371bd8adbccee5dace37b32f56d07ed635c7d2bc6397070303a2c9fc3679d0ac153c518de; TSf455e12a027=0804a8c53bab20002ae5fbe5591bf95371d77f48129a874f2aa422741c69a9788870759c631c3e4d08e768a11b113000d2d44fb1c9ad9663e86ff21ea4194585c1d55f0573642a7db52c5b7dcb66cb38b144590eecb391d6eddfd6847478251a'
    }

    post_template = Template(
        "{\"dates\":[\"$date\"],\"facilityId\":\"$facilityId\",\"positionId\":\"$positionId\",\"x\":$x,\"y\":$y,\"code\":\"$code\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"$date\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}")

    message_title_template = Template("Desk available $date ,$floor ...")
    message_txt_template = Template("Date $date \n Floor $floor \n Desk $code \n ")
    mail_success_template = Template("Desk $code booked for Date $date.")


