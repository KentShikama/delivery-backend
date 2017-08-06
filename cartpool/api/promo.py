if promo_code.type == "15% off" and store == "...":
    delivery_cost = management_cut + driver_cut
    percentage_of_delivery_cost = PERCENT * delivery_cost
    if management_cut > percentage_of_delivery_cost:
        management_cut -= percentage_of_delivery_cost
    else:
        driver_cut = driver_cut - percentage_of_delivery_cost + management_cut
        management_cut = 0
        # save both