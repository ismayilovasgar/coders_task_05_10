# *İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
# Metod olaraq 3 fərqli metoddan istifadə edəcəyik: Balansı artırmaq,  Pul çıxarmaq  və balansı göstərmək üçün metodlar.
# İkinci classımız isə kreditlə bağlıdır İlk classımızı bu classa inheritance eliyəcəyik və  super initdən  istifadə edəcəyik.
# Bu classda bizim 2 metodumuz olacaq. Kredit vermək və kredit ödənişi. Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.
# Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür və faiz yoxdur (kreditinməbləği / 12 = aylıq ödəniş).


class Hesab:
    def __init__(self, hesab_no, balans=0):
        self.hesab_no = hesab_no
        self.balans = balans
        self.is_allowed = False
        return self

    def __str__(self) -> str:
        return f"hesab no: {self.hesab_no}  balans: {self.balans}"

    def balans_artirmaq(self, miqdar):
        self.balans += miqdar
        print(f"hal-hazirdaki balans:{self.balans}")
        return self.balans

    def pul_cixarmaq(self, miqdar):
        self.balans -= miqdar
        print(f"cixarilan:{miqdar}\nbalans:{self.balans}")
        return self.balans

    def balans_gostermek(self):
        print(f"balansiniz:{self.balans}")
        return self.balans


class Kredit(Hesab):

    def __init__(self, hesab_no, balans=0):
        self.illik = 12
        self.kredit_meblegi = 0
        self.odenilen_mebleg = 0
        # self.borc = self.kredit_meblegi - self.odenilen_mebleg
        self.ayliq_odenis = self.kredit_meblegi / self.illik
        self.count = 1
        self.aylar_odenis = [(self.ayliq_odenis * k) for k in [*range(1, 13)]]
        super().__init__(hesab_no, balans)

    def kredit_goturmek(self, goturululen_mebleg):

        if not self.kredit_meblegi:
            if goturululen_mebleg > 0:
                self.kredit_meblegi = goturululen_mebleg
                print(f"Kredit Goturuludu, borcunuz: {self.kredit_meblegi} AZN")
                self.ayliq_odenis = self.kredit_meblegi / self.illik
                self.is_allowed = True
                return True

            else:
                print("meblge dogru daxil olunmayib")
                return False
        else:
            print(f"ugursuz emeliyyat, kreditiniz movcuddu:{self.kredit_meblegi} AZN")
            return False

    ##
    ##
    ##
    def krediti_goster(self):
        if self.is_allowed:
            self.borc = self.kredit_meblegi - self.odenilen_mebleg

            print(f"Kredi borcunuz:{self.borc}")
            return True
        else:
            print("ugursuz emeliiyat")
            # self.is_allowed = False
            return False

    def krediti_odemek(self, daxiledilen_mebleg):
        self.borc = self.kredit_meblegi - self.odenilen_mebleg
        if self.is_allowed:
            if (
                self.odenilen_mebleg >= self.aylar_odenis[self.count - 1]
            ) or self.odenilen_mebleg == 0:
                if daxiledilen_mebleg <= self.balans:

                    if daxiledilen_mebleg >= self.ayliq_odenis:

                        self.balans -= daxiledilen_mebleg
                        self.odenilen_mebleg += daxiledilen_mebleg
                        self.borc = self.kredit_meblegi - self.odenilen_mebleg
                        self.count += 1

                        if self.borc > 0:
                            print(f"ugurludu,kredit borcunuz:{self.borc:.2f} AZN")

                        elif self.borc < 0:
                            print(f"artiq daxil olunub, borcunuz:{self.borc:.2f} AZN")

                        else:
                            print("kreditinz baglandi...")
                            self.is_allowed = False

                    else:

                        if daxiledilen_mebleg == self.borc:
                            print("Kredit borcunuz baglandi.")
                            self.is_allowed = False
                            return True
                        else:
                            print("Mebleg ayliq odenisden azdi ")
                            return False
                else:
                    print(f"balansda bele mebleg movcud deyil")
                    return False

            else:
                print(
                    f"ayliq  meblegden azdi, min:{self.aylar_odenis[self.count-1] - self.odenilen_mebleg} AZN "
                )
                return False
        else:
            print("kredit ucun muracite edin....")

    ##
    ##
    ##


kredit = Kredit(10, 2000)
kredit.kredit_goturmek(1200)
kredit.krediti_goster()
kredit.krediti_odemek(1150)
kredit.krediti_odemek(50)
kredit.krediti_goster()
kredit.krediti_odemek(50)
