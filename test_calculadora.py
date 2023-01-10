import math


def comision_broker(sell_price, min_price):
    """
        This function calculates the broker's commission for
         every 200 sold 100 bonds without prorating
    Args:
        sell_price ():
        min_price ():

    Returns:
        message: message of status of commission
        success: True if commission is valid, False otherwise
    """
    percentage_bono_broker = (sell_price - min_price) / 200
    print(percentage_bono_broker)
    percentage_bono_broker = math.floor(
        percentage_bono_broker
    ) if percentage_bono_broker >= 0 else math.ceil(percentage_bono_broker)
    print(percentage_bono_broker)
    comision = percentage_bono_broker * 100
    print(comision)

    if comision >= 0:
        comision = format(comision, ",").replace(",", ".")
        message = f"Aprobado: Bono ${comision}"
        success = True
    else:
        comision = format(abs(comision), ",").replace(",", ".")
        message = f"Rechazado: Castigo a comisión ${comision} Si quiere legalizar" \
                  f"una oferta con este precio, debe solicitar una aprobación a BO."
        success = False

    return message, success


prueba = comision_broker(2000, 3000)
print(prueba)
