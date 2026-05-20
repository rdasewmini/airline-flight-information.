
des=[]
air_id=[]
seat_cpct=[]
cap_name=[]
trans=[]
avalable=[]

for i in range(10):
    print("\nflight",i+1)
    des=input("enter destination")
    air_id=int(input("enter aircraft ID"))
    seat_cpct=int(input("enter seat capacity"))
    cap_name=input("enter capton name")
    transits=int(input("enter transits"))

    avalable=bool(int(input("avalable?(1=yes,0=no)")))

    print("destination",des)
    print("aircraft ID",air_id)
    print("seat capacity",seat_cpct)
    print("captain name",cap_name)
    print("tansits",trans)

    if avalable:
        print("flight avalable")
    else:
        print("flight not avalable")
