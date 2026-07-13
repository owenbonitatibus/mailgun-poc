Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
KeyboardInterrupt
...                     text-align: center;
...                     padding-top: 100px;
...                 }
...                 .box {
...                     background: white;
...                     padding: 40px;
...                     margin: auto;
...                     width: 400px;
...                     border-radius: 10px;
...                     box-shadow: 0 0 10px rgba(0,0,0,0.1);
...                 }
...                 h1 {
...                     color: #333;
...                 }
...                 p {
...                     color: #666;
...                 }
...             </style>
...         </head>
...         <body>
...             <div class="box">
...                 <h1>PoC by Owen Bonitatibus</h1>
...                 <p>This subdomain was vulnerable to a Mailgun-based takeover.</p>
...             </div>
...         </body>
...     </html>
...     """
...
... if __name__ == "__main__":
...     app.run(host="0.0.0.0", port=8080)