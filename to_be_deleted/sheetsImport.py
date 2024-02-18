import gspread

creds = {
  "type": "service_account",
  "project_id": "prepdiscordbotproject",
  "private_key_id": "5da8c9683d12c3075e75278ac934462b522cf418",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC96fbIcb5wlPJz\n05X+DYOckHaRrwsfDXeyFtMyeZM5/+6i53pDUh5kkoY+OI9abQUqcR2bYfsysIYl\nsnddb4QCWZKk/kECx1MGrWk3Laz1N0HRHPdKASjbluo3mDi0w8bGW93IFK7uO0iK\nrre5rXsVICKjfSnMUVNLJ+ywvL3lC3ajo6IT4FPYnEQt+3upWgfT0/w7S7liYVnr\nArO4ZhBOh0jdM9T036R8oGyZD73doFMwmg9HD26dGPf5mUICSHaT+bDEb6W87jXl\nlvVvngkIM7aZMIg6vrX9tmSF5+NQMDCsDgJvl9aOvXaFym5yDk68oN/HBPePIfdz\nbUzO4gFJAgMBAAECggEABlbWMObSZsh4rFhCdYu8Gisx+KxuswS8e1fAM9CI6Hgh\nc34bCmlmECYvmsmWsrvDXvaOI1w6qec9tGntNT5ORNQlF+Klxw2MuQMWU+waIx2g\nUeDaj0rpHc//NZ0G6DUbFY7GS9IG7Hb9oFAd3Ac3/c1IDWGAQOybsBKfLQoWePFM\nNims3FvEPR6BXIsr+DHxN/opACRvhS9ry6KmyCmXan9dxzxzzl/qN5BRv7gE4yrk\n4KxIaA7nRnF2Fw1E18/MwWqfSIfqTKE7ulcJTS0X8BHIEaCYDR6eDgQsxZKt0Eng\nXh6mxPT0h41je/An1fS+NhTXETfHBJivkgj97jVqIQKBgQDdutLhumZVINvgdIEG\nLrjU1kByntd2IU/M4SiSvAEl3CyMOyX7PvydlOeeBR+nPwfPMnYT6ZAhV+tP7G5I\nLakQFTUFoaDmCH0tvcg/TacnKgkaBdEoz9AzRWh+/fXZvIHwYPO3AIj6qLML7xK5\nJzvCgPsSbrtrK57HGWjYuFFsmQKBgQDbREh0W6BoEoYfoVkWAz8EK7otd9BF/Xb5\nXfCqadsXWqI+zPSY97ddwlGVl6k3w6ZUMzYy+GQkedw7qARcSYNWAivewUOoAw7z\n+tHdQxqwJwv734vDMdzZTVi8g6uLLNVPJWixvT4tZS/tlpgPY0VyJb0Xj4V3ZczC\nDNAtTdj4MQKBgEC8UOFyiHoGM+veV+U0MuaA/yP32DQ3GZNZkXz1wugI1kDC7B3k\nj+B6Hv11xX4Q2vjVZL//iwMRJjSZdMFCA4AckPRp8g33IIUASbyhsVGv5iRg2mYt\n9j1h4FZjUyoU7WL/C2i8kUGNi2jKjg7cs4fgHG2PQszRWXQLqR7NAYjRAoGABV+I\n/wD3z1UU4FWN31I5CxsfNtoGypBJiBbbPPHXIp1f+HYBUHZRkgSfBzFuPiWXP9z5\naQpZOeOamAOoB7LtewAWnyDRTZ61kRkGZ4urbcGnM4bo3+Gq7dBNamE3pPN2Trg1\n9pUSnv4pzIKyOz5Nh1yRY7BqruBZwi+aMmID/SECgYEApKnBFD8rSFbnZNxo4HR/\nz24l5FGWadWqU7TY5piLhtpvHdUZF6YkI4+mzAdIK+wM/Qu7iJhd4mcmzTS9Cafr\nSx7uSoGRWozKwr+nQhoLc9abbFZtayRlEfU3+IVuyo4nEqIkEkVIFwgjDUV39/wq\nod7RI/uMBUQXI2/NFv4+LFY=\n-----END PRIVATE KEY-----\n",
  "client_email": "discordbot@prepdiscordbotproject.iam.gserviceaccount.com",
  "client_id": "113130043851925187344",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/discordbot%40prepdiscordbotproject.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

def getValues(BDD_name, sheet_name, sheet_range):
	"""
    Cette fonction accède à la BDD googlesheets et renvoie en raw les valeurs contenues dans la feuille passée en paramètre

    Parameters:
    BDD_name : le nom de la googlesheet de la BDD
    sheet_name : le nom de la feuille de la BDD dont on doit récup les valeurs
    sheet_range : les colonnes de la BDD à récupérer

    Returns:
    liste de valeurs : la liste raw des valeurs contenus dans la feuille en question
    """

	gc = gspread.service_account_from_dict(creds)
	sh = gc.open(BDD_name)

	return sh.worksheet(sheet_name).get(sheet_range)


def writeValues(BDD_name, sheet_name, sheet_range, values):
	"""
	Cette fonction accède à la BDD googlesheets et y écrit les valeurs contenues dans values

    Parameters:
    BDD_name : l'id du googlesheet de la BDD
    sheet_name : le nom de la feuille de la BDD dans laquelle on doit écrire les valeurs
    sheet_range : les colonnes de la feuille en question
    values : la liste raw des valeurs à écrire

    Returns:
    none
    """
	
	gc = gspread.service_account_from_dict(creds)
	sh = gc.open(BDD_name)

	sh.worksheet(sheet_name).update(sheet_range,values)