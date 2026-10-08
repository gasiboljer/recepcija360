from app import app, db, Soba  # Prilagodi uvoz ovisno o strukturi tvog projekta

def seed_bazu():
    with app.app_context():
        # Brišemo postojeće sobe da izbjegnemo duplikate
        db.session.query(Soba).delete()
        
        sobe_podaci = [
            # --- 1. KAT / SPRAT (Stara soba) ---
            {"broj_sobe": "101", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "102", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "103", "kapacitet": 3, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": True},
            {"broj_sobe": "104", "kapacitet": 1, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "105", "kapacitet": 1, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "106", "kapacitet": 1, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "107", "kapacitet": 1, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "108", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "109", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "110", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},

            # --- 2. KAT / SPRAT (Bez 206) ---
            {"broj_sobe": "201", "kapacitet": 2, "tip_kreveta": "Bračni krevet", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "202", "kapacitet": 2, "tip_kreveta": "Bračni krevet", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "203", "kapacitet": 2, "tip_kreveta": "Bračni krevet", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "204", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "205", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "207", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "208", "kapacitet": 2, "tip_kreveta": "Bračni krevet", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "209", "kapacitet": 2, "tip_kreveta": "Bračni krevet", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "210", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "211", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "212", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "214", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "215", "kapacitet": 4, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "216", "kapacitet": 3, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": True},
            {"broj_sobe": "217", "kapacitet": 3, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": True},

            # --- 3. KAT / SPRAT (Bez 306, s rezervnim 309 B i 310 B) ---
            {"broj_sobe": "301", "kapacitet": 3, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "302", "kapacitet": 3, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "303", "kapacitet": 3, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "304", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "305", "kapacitet": 2, "tip_kreveta": "Odvojeni kreveti", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "307", "kapacitet": 3, "tip_kreveta": "Bračni krevet", "kategorija": "Stara soba", "ima_bide": False},
            {"broj_sobe": "308", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "309", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "309 B", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "310", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "310 B", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "311", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": True},
            {"broj_sobe": "312", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "313", "kapacitet": 2, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
            {"broj_sobe": "315", "kapacitet": 3, "tip_kreveta": "Bračna odvojiva", "kategorija": "Nova soba", "ima_bide": False},
        ]

        for podaci in sobe_podaci:
            soba = Soba(
                broj_sobe=podaci["broj_sobe"],
                kapacitet=podaci["kapacitet"],
                tip_kreveta=podaci["tip_kreveta"],
                kategorija=podaci["kategorija"],
                ima_bide=podaci["ima_bide"],
                status="Slobodna"
            )
            db.session.add(soba)
        
        db.session.commit()
        print("Baza uspješno ažurirana i napunjena novim podacima!")

if __name__ == "__main__":
    seed_bazu()