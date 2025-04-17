import requests
def test_multiply(a,b):
    res=requests.post("https://super-duper-barnacle-gvvp594w9wg29gr6-8000.app.github.dev/multiply", json={"a":a ,"b":b})
    print("Request:", res.request.body)
    if res.status_code == 200:
        print("Multiply result:", res.json())
    else:   
        print("Error:", res.status_code, res.text)
    return res.json()       

if __name__ == "__main__":
    test_multiply(9,5)