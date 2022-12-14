import math


def comision_broker(self, min_price ):
    min_price = 1000
    sell_price = 1879
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
        message = f"Rechazado: Castigo a comisión ${comision} Si quiere legalizar una oferta con este precio, debe solicitar una aprobación a BO."
        success = False

    return message, success

prueba =  comision_broker(self=2000, min_price=1000)
print(prueba)