import datetime

html_start = """<!DOCTYPE html>
<html>
<head>
<title>Test Page</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Who is home?</h1>\n"""

time = "<p>Updated: {}</p>\n".format(datetime.datetime.now())

html_dynamic = '<ul>\n'

html_end ="""</ul>
</body>
</html>"""