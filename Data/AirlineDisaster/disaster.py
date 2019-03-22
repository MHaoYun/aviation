import requests
import json

airlines = [('Aeroflot', 'AFL'), ('Air France', 'AFR'), ('American Airlines', 'AAL'), ('Lufthansa', 'DLH'),
            ('Philippine Air Lines', 'PAL'), ('United Air Lines', 'UAL'), ('KLM', 'KLM'), ('Delta', 'DAL'),
            ('SAS', 'SAS'), ('All Nippon', 'ANA'), ('Alitalia', 'SMX'), ('China Airlines', 'CAL'),
            ('Air Canada', 'ROU'), ('Swiss', 'SWR'), ('British Airways', 'BAW'), ('Thai Airways', 'THA'),
            ('Turkish Airlines', 'THY'), ('Qantas', 'QFA'), ('Mongolian', 'MGL'), ('Singapore Airlines', 'SIA'),
            ('Lion Air', ''), ('China Eastern', ''), ('Xiamen Airlines', ''), ('Royal Nepal Airlines', ''),
            ('Air China', ''), ('Asiana', ''), ('Cathay Pacific', ''), ('Malaysia Airlines', ''),
            ('United Parcel Service', ''), ('China Southern Airlines', ''), ('Air New Zealand', ''),
            ('Emirates', ''), ('SriLankan Airlines', ''), ('Air Niugini', ''), ('Vietnam Airlines', ''),
            ('Air India', ''), ('Austrian Airlines', ''), ('Finnair', ''), ('Jet Airways', ''),
            ('Hainan Airlines', ''), ('AirAsia', ''), ('Sichuan Airlines', ''), ('EVA Air', ''), ('Joy Air', ''),
            ('Air Nippon', ''), ('Indonesia AirAsia', ''), ('Shanghai Airlines', ''), ('Tianjin Airlines', ''),
            ('Ibex', ''), ('Jeju Air', ''), ('Air Koryo', ''), ('Mandarin', ''), ('Nippon Cargo', '')]

def disaster(airline, page):
    url = 'http://www.safetyflights.com/public/api/search'
    headers = {
        'Content-Type': 'application/json;charset = UTF - 8',
        'Host': 'www.safetyflights.com',
        'Origin': 'http: // www.safetyflights.com',
        'Referer': 'http: // www.safetyflights.com /',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    if page == 1:
        payloadData = { 'airline': airline[0] }
    else:
        payloadData = {
            'airline': airline[1],
            'page': page
        }
    request = requests.post(url, data=json.dumps(payloadData), headers=headers)
    try:
        if(request.status_code == 200):
            request.encoding = 'uft-8'
            data = request.json()
            # file.write(data)
            accidents = data.get('details')
            for i in range(10):
                accident = accidents[i]
                if accident == '':
                    return 0
                type = accident.get('Type') if accident.get('Type') else 'Unknown'
                flight_number = accident.get('Flightnumber') if accident.get('Flightnumber') else 'Unknown'
                date = accident.get('Date') if accident.get('Date') else 'Unknown'
                casualties = accident.get('Total') if accident.get('Total') else 'Unknown'
                s = ''
                if accident.get('Classification'):
                    reasons = accident.get('Classification')
                    for reason in reasons:
                        s += reason
                else:
                    s = 'Unknown'
                output = "Type:"+type+" FlightNumber:"+flight_number+" Date:"+date+" Casualties:"+casualties+" Reason:"+s
                file.write(output+'\n')
        else:
            return 0
    except:
        print("error")
        return 0
    else:
        print("success")
        return 1

file = open('disaster.txt', 'w', encoding='utf-8')
for airline in airlines:
    # if airline == 'Aeroflot':
    #     file.write(airline + ':\n')
    # else:
    #     file.write('\n\n\n' + airline + ':\n')
    page = 1
    while True:
        if disaster(airline, page) == 0 or page >= 70:
            break
        page += 1
file.close()



