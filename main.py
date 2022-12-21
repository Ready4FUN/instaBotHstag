from instaBotHahstag import Client
import time 
import mariadb
import sys
import random

try:
    conn = mariadb.connect(
        user="root",
        password="1488",
        host="localhost",
        port=3306,
        database="insta"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# Get Cursor
cur = conn.cursor()

hashtag = ("беглов")

cl = Client()

cl.login("juravl46@gmail.com", "qwertyu2")


for tag in hashtag:
    medias_top = cl.hashtag_medias_top(tag, amount=9)
    medias = cl.hashtag_medias_recent(tag, amount=5)


    for media in medias_top:
        time.sleep(random.uniform(9, 25))
        print("next comment")
        media_id = media.dict()["id"]
        comments = cl.media_comments(media_id, amount=0) # amount = 0 - all comments
    
        cur.execute("INSERT INTO hashtag (url,datetime) VALUES (?, ?)", 
        ("https://www.instagram.com/" + str(media.dict()['code']), str(media.dict()['taken_at']))) #all you date need
        
        conn.commit()
        
        '''
        {'pk': 2574092718364154697,
        'id': '2574092718364154697_376712420',
        'code': 'CO5A7BxA9tJ',
        'taken_at': datetime.datetime(2021, 5, 15, 10, 49, 45, tzinfo=datetime.timezone.utc),
        'media_type': 1,
        'product_type': '',
        'thumbnail_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/186430270_473573763896149_2030909827389015824_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=4jFHY_INCnMAX-7fObK&edm=AP_V10EBAAAA&ccb=7-4&oh=9fb0c4cdb01a7aa376a96c0df366d844&oe=60C4C01A&_nc_sid=4f375e', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/s1080x1080/186430270_473573763896149_2030909827389015824_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=4jFHY_INCnMAX-7fObK&edm=AP_V10EBAAAA&ccb=7-4&oh=9fb0c4cdb01a7aa376a96c0df366d844&oe=60C4C01A&_nc_sid=4f375e'),
        'location': {'pk': 517543,
        'name': 'Sestola',
        'address': '',
        'lng': 10.77328,
        'lat': 44.2266,
        'external_id': 103150459725396,
        'external_id_source': 'facebook_places'},
        'user': {'pk': 376712420,
        'username': 'vascobica',
        'full_name': '⚡Vasco Bica®⚡',
        'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/96211403_922669918147090_5138958292701151232_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tYlGX8kDuSgAX9WtBRF&edm=AP_V10EBAAAA&ccb=7-4&oh=ac96c75846d17519e53923a0ddb3aad0&oe=60C51486&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/96211403_922669918147090_5138958292701151232_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tYlGX8kDuSgAX9WtBRF&edm=AP_V10EBAAAA&ccb=7-4&oh=ac96c75846d17519e53923a0ddb3aad0&oe=60C51486&_nc_sid=4f375e'),
        'stories': []},
        'comment_count': 8,
        'like_count': 327,
        'has_liked': None,
        'caption_text': 'Ready to fight ⚔️\n#js7 \n.\n.\n#swissmountainsports #racing #coppaitaliadh \n#mirandabikeparts\xa0#burning\xa0#jumping \xa0#whipit\xa0#scrubit\xa0#enduro\xa0#mtblife\xa0 #downhill\xa0#mountainbiking\xa0#sliding\xa0#dirt\xa0#dh\xa0 #mtb\xa0#bike\xa0#bikelife\xa0#friends\xa0#mtbswitzerland\xa0#downhillmtb\xa0#valais\xa0 #swissmountains\xa0\xa0#italy #italydownhill',
        'usertags': [{'user': {'pk': 3636959873,
            'username': 'christopherstrm',
            'full_name': 'Christopher Ström',
            'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/173775865_527371595096868_8991176723035066304_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tbsAzTDoLtEAX_HaT9Z&edm=AP_V10EBAAAA&ccb=7-4&oh=94a18b3b4d0d39d9dbda849b4c23a5a9&oe=60C5192F&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/173775865_527371595096868_8991176723035066304_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tbsAzTDoLtEAX_HaT9Z&edm=AP_V10EBAAAA&ccb=7-4&oh=94a18b3b4d0d39d9dbda849b4c23a5a9&oe=60C5192F&_nc_sid=4f375e'),
            'stories': []},
        'x': 0.211352657,
        'y': 0.8478260870000001}],
        'video_url': None,
        'view_count': 0,
        'video_duration': 0.0,
        'title': '',
        'resources': []}
        '''

        for media in medias:
            time.sleep(random.uniform(9, 25))
            media_id = media.dict()["id"]
            comments = cl.media_comments(media_id, amount=0) # amount = 0 - all comments
        
            cur.execute( "INSERT INTO hashtag (url,datetime) VALUES (?, ?)", 
            ("https://www.instagram.com/" + str(media.dict()['code']), str(media.dict()['taken_at']))) #all you date need
            
            conn.commit()