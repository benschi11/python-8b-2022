input_string = "1,A,5,B,10,A,8,A,17,B,17"

bids = input_string.split(",");
start = int(bids[0]); # Startgebot
# Lösche Startgebot
bids.pop(0);

# Setze Startwerte
current_bid = start;
maxbid = 0;
maxbidder = None;


end = int(len(bids)/2)

for i in range(0,end):
    bidder = bids[2*i];
    bid = int(bids[2*i+1]);
    if current_bid < bid:
        if maxbid < bid: # neue Maximalgebot, 
            maxbidder = bidder; # neuen Maximalbieter
            current_bid = maxbid+1;
            maxbid = bid; # neues Maximalgebot

        elif(maxbid == bid):
            current_bid = maxbid;
        else:
            current_bid = bid + 1;


print(maxbidder + "," + str(current_bid))

#print(",".join(history));

