from string import Template


class Parameters:

    date_strings = ['2024-11-20', '2024-11-21', '2024-11-22']

    planner_url = "https://myplanner.netcompany-intrasoft.com"

    available_seats_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/facility/facilities/available/map"

    my_booked_desks_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/future?page=0&size=15"

    find_desk_booking_id_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/calendar"

    put_url = Template("https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/$deskbookingid/edit")

    headers = {
        'Content-Type': 'application/json, text/plain, */*',
        'Cookie': 'Path=/; Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=0CBC02C4AC845EF525F3C49A21115865; TS010ee64b=01eb1053a051ad8056b4ad440817587916fd52933deb353bbd3507629eaf1aee78ac173b22d8452eb7a97c3d73ba37aa49b873f43f3b53df5c3df742f86502c60cc69c866dd1a0eb9de452532d6ef069a81592a7e5; TSf455e12a027=0804a8c53bab2000bed0ee7bdf486517676bceaf7f9c94317dec601892194e39130c97b49b39ca2108d502629111300086b6bcaab909b44eb106927b690319043201a50229c3413e7f6dbde2a88d522ab07f22da49830240d894150f8324d26c'
    }

    put_template = Template(
        "{\"date\":\"$date\",\"facilityId\":\"$facilityId\",\"positionId\":\"$positionId\",\"x\":$x,\"y\":$y,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":{\"type\":\"0036\",\"date\":\"$date\"}}")

    message_title_template = Template("Desk available $date ,$floor ...")
    message_txt_template = Template("Date $date \n Floor $floor \n Desk $code \n ")
    mail_success_template = Template("Desk $code booked for Date $date.")


