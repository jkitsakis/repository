from string import Template


class Parameters:

    date_strings = ['2024-11-27']

    planner_url = "https://myplanner.netcompany-intrasoft.com"

    available_seats_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/facility/facilities/available/map"

    my_booked_desks_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/future?page=0&size=15"

    find_desk_booking_id_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/calendar"

    put_url = Template("https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/$deskbookingid/edit")

    referer_url=Template("https://myplanner.netcompany-intrasoft.com/booking/$deskbookingid/edit")

    get_my_booking_details_url = Template("https://myplanner.netcompany-intrasoft.com/booking/$deskbookingid")

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json, text/plain',
        'Cookie': 'Path=/; Path=/; Path=/; TS00000000076=0804a8c53bab280017ff39cef214f6c06c2c9648ba1d3ba9bd6ba3a28b8792d536e45a5ce0975ca37e37a6ca592ecd0e08112dd2f509d00004404e518c953404bca6a3dd64b9585007f5045aaee112b943a91558385e8adac8dca142f73b5486eeafb56daf8c046a5e0bea8e588c188bb5f4046cc0e09ab58f4b1881a6052a346dc52cabf275583b98d27f0c217acb64bf7318e15806b7545d41e6c2a4728ce9e43877a8fa3b0907a599a3fbb4784744433b6c166a8e93d75eb8f8d1bbbc60d221f82dc0b2da17c216b1646a1546fd8ce1465b7b4fdc40491d41deaeecf9cda7a0c42e183aa77d5458a4dabe6cb81dcbe62e29a1b4e916c5599086106657ab2ea442568aefa2f6d1; TSPD_101_DID=0804a8c53bab280017ff39cef214f6c06c2c9648ba1d3ba9bd6ba3a28b8792d536e45a5ce0975ca37e37a6ca592ecd0e08112dd2f50638004a88a0b68cab703c2a1a033abc770cdf2fe21e334bac6744d0a6e47788fe6153643a49a271d6a446e08bc735916ae0695488c214f7aa08b4; JSESSIONID=C9E82643E0EFF89732983263FA81C703; TS010ee64b=01eb1053a0c65ca987e29da224eb5780e9829e0c1445b8cbdd5ede930bde0ff08c655d3343cf9150cd04122947e3c3d76fed1a1ef150af358394d0af8a57d85877352943935daa87ffea2fb73ef2914d8852d6f74f; TSf455e12a027=0804a8c53bab20005d3bc082c37ee1b885ec947be24dc36cd7fb4725477c75f52076391f596ce22108ca5b09291130005a3a046c935a058f2a13577b602fbba07827247c66686c7ccdeb0799be63a50f01794a8207a8c33473ce3fe2bb729524'
    }

    put_template = Template(
        "{\"date\":\"$date\",\"facilityId\":\"$facilityId\",\"positionId\":\"$positionId\",\"x\":$x,\"y\":$y,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":{\"type\":\"0036\",\"date\":\"$date\"}}")

    message_title_template = Template("Desk available $date ,$floor ...")
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
