import feedparser

somjang_blog_rss_url = "https://rbsks.tistory.com/rss" # 티스토리 rss
rss_feed = feedparser.parse(somjang_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 5 # 여기 최대 값

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}.{feed_date.tm_mon}.{feed_date.tm_mday} -  {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """
<h2>⚙️Skill</h2>
<section>
<h3>BackEnd</h3>
<div>
    <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-sqaure&logo=coffeeScript&logoColor=white">
    <img src="https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-sqaure&logo=springBoot&logoColor=white">
    <img src="https://img.shields.io/badge/Spring%20REST%20Doc-6DB33F?style=flat-sqaure&logo=spring&logoColor=white">
    <!-- <img src="https://img.shields.io/badge/Spring%20Security-6DB33F?style=flat-sqaure&logo=springSecurity&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/Spring%20Batch-6DB33F?style=flat-sqaure&logo=bookStack&logoColor=white"> -->
    <img src="https://img.shields.io/badge/Spring%20Data%20JPA-6DB33F?style=flat-sqaure&logo=hibernate&logoColor=white">
    <img src="https://img.shields.io/badge/QueryDSL-5d9bb9?style=flat-sqaure&logo=ApacheECharts&logoColor=white">
    <!-- <img src="https://img.shields.io/badge/Json%20Web%20Token-442e2e?style=flat-sqaure&logo=jSONWebTokens&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/OAuth2-EC1C24?style=flat-sqaure&logo=Authy&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-sqaure&logo=rabbitMq&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/Stomp-3b5c6b?style=flat-sqaure&logo=Lospec&logoColor=white"> -->
</div>
<h3>DataBase</h3>
<div>
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-sqaure&logo=mysql&logoColor=white">
    <img src="https://img.shields.io/badge/MariaDB-1F305F?style=flat-sqaure&logo=mariadb&logoColor=white">
    <!-- <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-sqaure&logo=redis&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/Mongo%20DB-47A248?style=flat-sqaure&logo=mongoDb&logoColor=white"> -->
</div>
<!-- <h3>Production</h3> -->
<!-- <div> -->
    <!-- <img src="https://img.shields.io/badge/Amazon%20Web%20Services-232F3E?style=flat-sqaure&logo=amazonAWS&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=flat-sqaure&logo=amazonEC2&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/AWS%20S3-569A31?style=flat-sqaure&logo=amazonS3&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/AWS%20RDS-527FFF?style=flat-sqaure&logo=amazonRDS&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/NGINX-009639?style=flat-sqaure&logo=nginx&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-sqaure&logo=Jenkins&logoColor=white"> -->
    <!-- <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-sqaure&logo=docker&logoColor=white"> -->
<!-- </div> -->
</section>
<h2>🧱Git status</h2>

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=rbsks&show_icons=true&theme=default)<br>

<h2>🖌 PS</h2>

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=rbsks0302)](https://solved.ac/rbsks0302/)

<h2>📒Blog status</h2>

📖[규난 블로그 보러 가기](https://rbsks.tistory.com/)


"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
