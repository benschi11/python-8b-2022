input_string = input();

bids = input_string.split(",");
start = int(bids[0]); # Startgebot
# History für Level 3
history = [];
# Lösche Startgebot
bids.pop(0);

# Setze Startwerte
current_bid = start;
maxbid = 0;
maxbidder = None;
firstbid = True;

history.append("-," + str(current_bid));

end = int(len(bids)/2)

for i in range(0,end):
    bidder = bids[2*i];
    bid = int(bids[2*i+1]);
    if current_bid < bid or (current_bid == bid and firstbid):
        if maxbid < bid:
            if firstbid and current_bid == bid:
                maxbidder = bidder;
                current_bid = bid;
                history.append(maxbidder+","+str(current_bid));
            if bidder != maxbidder:
                maxbidder = bidder;
                current_bid = maxbid+1;
                history.append(maxbidder+","+str(current_bid));

            maxbid = bid;
            firstbid = False;

        elif(maxbid == bid):
            current_bid = maxbid;
            history.append(maxbidder+","+str(current_bid));
        else:
            current_bid = bid + 1;
            history.append(maxbidder+","+str(current_bid));


# print(maxbidder + "," + str(current_bid))

print(",".join(history));

