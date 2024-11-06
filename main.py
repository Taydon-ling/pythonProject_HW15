def errorcode(x):
    match x:
        case 500:
            return("Internal Server Error")
        case 401:
            return("Unauthorised")
        case 400:
            return("Bad Request")
        case 403:
            return("Forbidden")
        case 404:
            return("Not Found")
        case 501:
            return("Not Implemented")
        case 502:
            return("Service Temporarily Overloaded")
        case 501:
            return("Service Unavailable")

x = int(input("What does the error say? "))
print("It means", errorcode(x))