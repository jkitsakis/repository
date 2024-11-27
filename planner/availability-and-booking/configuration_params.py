from string import Template


class Parameters:

    # date_strings = ['2024-11-28']
    date_strings = ['2024-12-02','2024-12-03','2024-12-05','2024-12-06']

    cookie = 'Path=/; Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=90F817159AACF58CADC0DB555AB49D3D; TS010ee64b=01eb1053a0e0713e8f270c995c0bd6f47a135f00018a5d0757f78f68cf1c76abc73b29753d30381e0689ceae158123e654042a67f592217e2b48e8938123aba69a70298092fe967142dabf3e55b8fe77b84942c44f; TSf455e12a027=0804a8c53bab20006ab196a4697679331da38dc6413244b818737ef6a3116d41745c3580cd2cc72c08b27018d1113000d65cafce01da141dbded7619c957f4ce3c8781e507f02768cd87bbe5715a3793aa1ad3828d2ade4602f2b0aa22db6b61'

    planner_url = "https://myplanner.netcompany-intrasoft.com"

    available_seats_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/facility/facilities/available/map"

    my_booked_desks_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/future?page=0&size=15"

    find_desk_booking_id_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/calendar"

    # put_url = "https://httpbin.org/put"
    put_url = Template("https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/$deskbookingid/edit")

    post_url = "https://httpbin.org/post"
    # post_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"

    referer_url=Template("https://myplanner.netcompany-intrasoft.com/booking/$deskbookingid/edit")

    get_my_booking_details_url = Template("https://myplanner.netcompany-intrasoft.com/booking/$deskbookingid")

    get_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'myplanner.netcompany-intrasoft.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Cookie': cookie
    }
    put_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'myplanner.netcompany-intrasoft.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    post_headers = {
        'Content-Type': 'application/json',
        'Host': 'myplanner.netcompany-intrasoft.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    post_template = Template("{\"dates\":[\"$date\"],\"facilityId\":\"$facilityId\",\"positionId\":\"$positionId\",\"x\":$x,\"y\":$y,\"code\":\"$code\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"$date\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}")

    put_template = Template("{\"date\":\"$date\",\"facilityId\":\"$facilityId\",\"positionId\":\"$positionId\",\"x\":$x,\"y\":$y,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":null}],\"datesAndType\":{\"type\":\"0036\",\"date\":\"$date\"}}")

    message_title_template = Template("Desk available $date, on $floor ...")
    message_txt_template = Template("Date $date \n Floor $floor \n Desk $code \n ")
    mail_success_template = Template("Desk $code booked for Date $date.")


# PUT header example
# ------------------------
# PUT /deskbooking/api/v1/deskbooking/6734791f51c9872a34f817b7/edit HTTP/1.1
# Accept: application/json, text/plain, */*
# Accept-Encoding: gzip, deflate, br, zstd
# Accept-Language: en-US,en;q=0.9,el;q=0.8
# Connection: keep-alive
# Content-Length: 236
# Content-Type: application/json;charset=UTF-8
# Cookie: Path=/; Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=0CBC02C4AC845EF525F3C49A21115865; TS010ee64b=01eb1053a0db53ab362ca919a0b99e277ea0c136b2e7f4c8bbec65404000b9f8541b7706b39c76c5e626a544db330477ccdb1c5ec5fcda5f737367a1080fc5b5c3b8e8b4b49ad57d43f6c8d870e0821ec6b6cf3dc8; TSf455e12a027=0804a8c53bab200093744f909cab38aa47be75070bc2297bb914a61c8b9e2f8d631f6fcf8c1ad6b708a830ff36113000015b7142929eaf0ad4dc83ff6ca0ebaed019a1550fa4725ce927357e84d20336fdf53d1a675c320e67b433be1fb633c5
# Host: myplanner.netcompany-intrasoft.com
# Origin: https://myplanner.netcompany-intrasoft.com
# Referer: https://myplanner.netcompany-intrasoft.com/booking/6734791f51c9872a34f817b7/edit
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
# sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
