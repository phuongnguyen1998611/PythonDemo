#nhan_doi = lambda a:a*2
#print(nhan_doi(4))

danh_sach = [1,2,3,4,5,6,7,8,9,10]
tap_hop = filter(lambda a:a%2==0, danh_sach)
print(list(tap_hop))

tap_hop_nhan_doi = list(map(lambda a:a*2, danh_sach))
print(tap_hop_nhan_doi)
#toi muon thay doi
