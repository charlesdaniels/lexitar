import unittest

import lexitar
import reedsolo

ipsum = """

Alias esse eos qui minus deserunt tempore est. Non totam cum repudiandae
repudiandae. Rerum consectetur pariatur nesciunt consequuntur distinctio in.
Consequatur suscipit iure commodi veniam et iste iure nostrum.

Sed id unde architecto. Dignissimos reprehenderit ex voluptas et non adipisci
modi aperiam. Fugiat sit dolorum pariatur aut qui porro quos enim. Tempora
autem repudiandae culpa vel excepturi. Distinctio in molestiae non quis ea
corrupti.

Error minima ut non a ut provident odio quaerat. Non possimus porro alias in
nam quia facere quod. Voluptatem excepturi praesentium autem ut distinctio
beatae nobis quo.

Aut illo repudiandae maiores. Est qui est aut culpa in optio id ut. Est vel
debitis fugiat accusamus expedita. Ut ut ut non porro delectus magni dolorem.
Natus illo est repellat velit explicabo exercitationem nam.

Quidem et eligendi ex voluptatem. Repudiandae eos provident maiores repudiandae
harum quia fugit non. Voluptatem dolores culpa tempora eum ut autem est. Enim
possimus itaque fugit deserunt maiores cum quo harum. Repudiandae ex et quia
nihil fuga.



Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in ante eget
sapien faucibus sodales molestie ut leo. Etiam elementum ante in tortor semper,
id pulvinar nisl maximus. Quisque ac diam eget augue facilisis pretium eget sit
amet eros. Praesent vitae nunc quis eros convallis accumsan nec vel nisi.
Nullam posuere lorem id tincidunt pulvinar. Morbi tortor nunc, tincidunt in
erat sed, congue tincidunt odio. Suspendisse vel nisl lacinia mi gravida
dapibus ac et quam. Sed bibendum orci ut leo placerat interdum. Pellentesque
sit amet commodo erat. Mauris varius feugiat augue, sit amet laoreet diam
tincidunt ut. Vivamus eu sodales leo, nec tristique mi. Proin diam nisl,
euismod sit amet commodo a, egestas porta leo. Nam mollis, ligula sit amet
facilisis ornare, lectus diam interdum sem, a blandit justo lacus ut sapien.
Nulla facilisi. Ut suscipit erat mi, non placerat tellus vehicula a.

Donec quis odio a neque blandit sollicitudin quis vitae magna. In fermentum
massa finibus velit molestie, eget ultrices libero laoreet. Nullam nec leo eget
urna gravida condimentum. Nulla ullamcorper sapien sagittis, egestas lorem sed,
dapibus nibh. Pellentesque sem velit, hendrerit sed augue at, maximus
condimentum sapien. Quisque accumsan tellus sed varius gravida. Nunc sit amet
imperdiet libero. Ut gravida egestas neque. Integer in pellentesque leo, in
egestas massa. Nulla velit lectus, imperdiet et fringilla sit amet, congue at
mauris. Maecenas fringilla, nulla vel sollicitudin consectetur, sem dui
pharetra dui, sit amet tempus urna ex ac elit. Phasellus vitae justo a nunc
fermentum faucibus nec interdum magna. Phasellus id nibh varius, tempor ligula
non, imperdiet ante. Suspendisse a mauris fringilla, lacinia justo ut, ornare
ante. Proin cursus mauris eu venenatis fringilla. Duis pharetra enim nibh, quis
consequat tortor rutrum non.

Vestibulum euismod risus ut commodo euismod. Nunc vestibulum maximus neque nec
posuere. Pellentesque eget ex elementum, posuere quam sit amet, facilisis
sapien. Vestibulum cursus tortor vel eros gravida, id tempor quam congue. Nam
id pellentesque velit. Sed dapibus ante sit amet dolor tempus, quis malesuada
enim placerat. Aenean sit amet orci pellentesque, tristique diam sed, bibendum
augue.

Nulla at odio orci. Nam efficitur imperdiet tellus, ut tempor orci aliquet et.
Donec ornare quam sit amet urna imperdiet, sed luctus dui ultrices. In rhoncus
ut eros a fermentum. Etiam at elit et erat ultrices rutrum. Vivamus at posuere
magna. Fusce rutrum nisi ornare, lobortis diam commodo, laoreet tortor. Nam
tristique, nunc quis iaculis accumsan, libero augue varius nisi, feugiat
placerat metus lacus pharetra metus. Mauris sit amet massa varius, ullamcorper
lacus vitae, vestibulum urna. Maecenas lacus urna, ultrices et luctus nec,
auctor eget libero. Donec ac erat et ipsum hendrerit fringilla nec ut risus.
Vestibulum nibh tellus, mattis vel lectus sed, convallis porta ex. Fusce
gravida placerat sapien, sed ultricies lacus faucibus vel. Aliquam pharetra
lorem felis, in euismod sapien tincidunt a. Vivamus fermentum, leo commodo
scelerisque sodales, velit arcu laoreet purus, a fermentum nisl tellus eu
felis. Praesent ac tellus commodo, fringilla mauris nec, tempor ex.

Suspendisse id leo ut enim euismod gravida. Sed non mauris at mauris dictum
hendrerit. Vivamus fermentum in quam sed malesuada. Mauris pharetra luctus
risus. In interdum tortor pretium lorem vulputate, a semper tellus hendrerit.
Aliquam vitae leo diam. Morbi gravida bibendum mauris non condimentum. Proin eu
facilisis tortor, ut posuere nunc. Sed tincidunt massa sit amet sapien
ullamcorper vulputate. Praesent porttitor non ligula et tristique.

Ut rhoncus sit amet purus quis vehicula. Vestibulum cursus tellus egestas
eleifend fermentum. Donec efficitur arcu quis arcu molestie rhoncus. Aliquam
egestas nisl nec arcu interdum, sit amet pretium urna condimentum. Pellentesque
in rutrum tortor. Vestibulum pulvinar turpis sit amet enim faucibus pharetra.
Vivamus elementum id ligula vitae porta. Suspendisse id imperdiet sem. Cras
aliquet eros orci, vitae scelerisque augue imperdiet quis. Suspendisse tempus,
tortor sit amet eleifend ultricies, leo felis scelerisque velit, eget tincidunt
eros felis a orci. Proin velit dui, dignissim vel metus eget, tempor
condimentum ante.

Curabitur tincidunt mollis est, non porta metus maximus vel. Maecenas sit amet
turpis et diam consectetur rutrum. Orci varius natoque penatibus et magnis dis
parturient montes, nascetur ridiculus mus. Integer lorem ante, pellentesque
eget euismod et, pretium at risus. Suspendisse sit amet porttitor nibh.
Vestibulum cursus mauris eros, eu volutpat lorem consectetur vel. Mauris id
enim sed ipsum bibendum accumsan eu placerat tortor. Nunc suscipit imperdiet
nibh in fermentum. Maecenas accumsan nisl eu fringilla egestas. Integer iaculis
accumsan quam, a vehicula nisi mollis sit amet.

Vivamus gravida feugiat nunc, sed efficitur purus sodales posuere. Aenean massa
est, mollis ac velit vel, interdum laoreet arcu. Vestibulum nec odio eget diam
cursus dignissim. Curabitur tempor felis in arcu molestie, et egestas nisl
fringilla. Nam sollicitudin lorem at justo fringilla, vel iaculis purus
sodales. Fusce eu enim quis justo mollis scelerisque. Sed ut sapien viverra,
placerat diam vitae, malesuada neque.

Proin in cursus erat. Nulla facilisi. Aliquam sagittis, velit vel tempus
ultrices, tellus diam feugiat velit, et pretium ante ex porttitor quam. Etiam
sed placerat velit. Etiam bibendum massa in neque vestibulum porttitor. Etiam
accumsan nisi eget tincidunt elementum. Mauris a augue eget ante facilisis
efficitur in quis tortor. Integer laoreet eget leo posuere vestibulum. Class
aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos
himenaeos. Proin mollis elementum elit, ac fringilla lectus molestie nec. Nunc
lobortis gravida sapien id tincidunt. Ut cursus lectus a leo fringilla feugiat.

Aenean tincidunt enim nec fringilla congue. Aenean porttitor sem id tortor
sagittis, eu lacinia libero lobortis. Nam suscipit erat sit amet rutrum
commodo. Donec et pretium tellus. Sed finibus imperdiet egestas. Orci varius
natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Mauris in lorem sodales purus luctus molestie ut non augue. Class aptent taciti
sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec
pulvinar ex erat, vitae pellentesque elit lacinia id. Vivamus nec justo at sem
vulputate volutpat sed scelerisque lectus.

Ut egestas quis nulla quis luctus. Suspendisse gravida congue nibh et lobortis.
Nulla augue urna, volutpat nec dapibus consectetur, tempus id neque. Donec
malesuada dictum euismod. Curabitur dignissim quam justo, ut efficitur nisl
placerat sollicitudin. Sed quis mattis eros. Maecenas bibendum sem ac massa
gravida, sit amet faucibus neque elementum. Nam et auctor quam, eget
sollicitudin magna. Nunc facilisis, quam sed pellentesque rhoncus, erat nunc
interdum turpis, quis faucibus erat lacus et odio. Nunc et facilisis augue, at
semper quam. Aliquam eu sapien et ipsum egestas mattis eu id turpis.
Suspendisse potenti. Curabitur fringilla quam massa, nec accumsan mauris
pellentesque pellentesque. Integer lorem elit, tempus nec consequat hendrerit,
aliquet quis tortor. Maecenas mattis mollis elit at pellentesque. Mauris
feugiat, felis vel pellentesque egestas, ante felis tempus felis, vestibulum
rutrum nisi elit eget sem.

Quisque neque neque, tempus vel dolor bibendum, euismod mattis magna. Phasellus
sed orci enim. Nunc vel eros et diam varius pharetra. Ut at nibh metus. Mauris
vulputate varius dolor vel dapibus. Suspendisse sed tristique ante. Vestibulum
ut consectetur felis. Nulla turpis augue, posuere at nisi non, pellentesque
lobortis ante. Vivamus vehicula iaculis odio.

Donec dapibus ullamcorper libero sed pellentesque. In at mollis lorem. Vivamus
a blandit nibh, in malesuada eros. Cras gravida mi vel imperdiet imperdiet.
Donec ultrices tempor purus ac tempor. Curabitur dictum ex in eros tempus, et
auctor ligula auctor. Phasellus turpis justo, fringilla vitae dapibus quis,
pulvinar quis magna. Vivamus eget purus maximus, consectetur mi id, rutrum
quam. Fusce eu enim semper, cursus lectus in, luctus elit. Vivamus vulputate
est a mi aliquet commodo. Nulla porttitor purus sit amet sem pharetra, a
malesuada mi egestas. Cras sollicitudin, libero nec euismod placerat, nisl est
malesuada magna, non sollicitudin nunc diam vel odio. Nam accumsan in lacus at
euismod. Sed vulputate lacus nec felis accumsan, at hendrerit nunc blandit.
Mauris commodo suscipit nisl nec accumsan.

Proin eget facilisis ante. Donec felis diam, convallis sed volutpat eleifend,
ultrices sit amet libero. Sed pharetra, massa et fermentum viverra, enim mi
dignissim mi, eu dictum urna ligula quis est. Donec eu nulla sed nisi dignissim
semper. Suspendisse iaculis, enim vitae vehicula dictum, risus enim placerat
arcu, at cursus lorem dolor sed diam. Aliquam commodo, nisl tempor suscipit
laoreet, dolor dui faucibus lorem, sed interdum velit ante quis nulla. In
tortor elit, molestie ac facilisis nec, placerat a est. Pellentesque varius
dolor eget erat imperdiet, non semper odio bibendum. Etiam cursus, magna id
pellentesque rhoncus, tellus neque cursus justo, sed consectetur mi mauris in
mi. Praesent ut ligula pulvinar, consectetur quam sed, pulvinar eros. Nullam
iaculis dui vel sollicitudin vehicula. Praesent ultricies ante sit amet enim
interdum tincidunt.

Etiam at lectus tellus. Nam porta mauris quis ipsum imperdiet rutrum. Mauris
nec nulla laoreet, ultrices arcu nec, venenatis elit. Aliquam erat volutpat.
Integer at placerat massa. Etiam nec accumsan quam. Praesent venenatis, mauris
a feugiat aliquam, erat mauris faucibus dui, vel ultrices massa arcu a lacus.
Praesent nec nisl ante.

Quisque molestie feugiat massa, sed tristique sapien iaculis eget. Phasellus
pellentesque ultricies auctor. Proin orci nibh, varius a mi non, condimentum
volutpat lectus. Vivamus faucibus sem ac sem ornare iaculis. Morbi posuere
augue quis tortor bibendum mollis. Nam feugiat turpis in ante ornare efficitur.
Duis non mauris lorem.

Etiam elit elit, accumsan ut dolor id, gravida hendrerit est. Pellentesque ut
cursus urna. Aliquam erat volutpat. Aenean accumsan nunc nec turpis lobortis,
sed malesuada elit accumsan. Curabitur eleifend ut elit eget egestas. Donec
eleifend nisi purus, a malesuada turpis hendrerit malesuada. Etiam leo felis,
euismod non feugiat id, vulputate eu justo. Praesent tempus, justo ut ultrices
condimentum, tellus neque consequat tellus, vitae iaculis neque lorem sed
tellus. Suspendisse pellentesque, ex vitae scelerisque egestas, purus velit
imperdiet nunc, at aliquet augue eros nec neque. Suspendisse egestas pharetra
tincidunt.

Phasellus vel semper justo. Praesent elementum mattis mi. Suspendisse nec
varius nibh. Donec ut consectetur justo, nec pulvinar nunc. Suspendisse
fringilla aliquet ex nec ullamcorper. Pellentesque id massa imperdiet, dictum
justo eget, auctor tortor. Morbi sit amet tempor eros. Morbi in pulvinar nibh.
Quisque mattis mi id tortor vestibulum facilisis. Cras vestibulum odio vel
gravida interdum. Maecenas ac felis et mi facilisis viverra eget sed arcu.
Suspendisse elementum risus ac gravida interdum. Duis ut metus sit amet lacus
gravida malesuada. Phasellus tincidunt, dolor ac congue ullamcorper, tortor
neque tincidunt magna, eu imperdiet elit eros sed nibh. Praesent tincidunt eros
quis leo malesuada lacinia. Proin mollis mollis molestie.

Orci varius natoque penatibus et magnis dis parturient montes, nascetur
ridiculus mus. Sed dui sapien, ornare laoreet eleifend sit amet, mattis eu
purus. Suspendisse molestie neque enim, eu sollicitudin nisi bibendum eget.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras egestas ante
vitae viverra aliquet. Curabitur id purus id orci sagittis tempor eget ut diam.
Praesent ut libero ac neque venenatis commodo.

Sed ut nulla at ligula scelerisque porta. Nunc sodales orci ac ligula eleifend
scelerisque. Ut non sem sit amet turpis varius cursus. Nullam mauris lorem,
pharetra sed ante eu, finibus vehicula risus. Aliquam ut aliquam ex. Donec
suscipit justo turpis. Quisque a posuere libero.

In id ultricies felis, at lobortis mi. Aenean dignissim dolor at turpis
pulvinar, at tincidunt nulla imperdiet. In hac habitasse platea dictumst.
Quisque consequat condimentum ipsum at pellentesque. Curabitur quis arcu quam.
Cras suscipit ac sapien hendrerit viverra. Suspendisse sed justo id sapien
ultricies accumsan. Praesent eros ante, congue id vestibulum tincidunt,
efficitur ac lorem. Donec ut mi ac est viverra pulvinar. Vivamus convallis
mattis mauris vitae euismod. Donec hendrerit cursus risus et luctus. Vestibulum
sodales vitae risus id viverra.

Maecenas gravida lorem ut purus pharetra dapibus. Fusce lobortis sit amet purus
sed pellentesque. Sed ornare risus sit amet tellus suscipit euismod. Vestibulum
mattis neque et urna blandit, eu ullamcorper lectus blandit. Nunc ligula neque,
fringilla at ligula vitae, tristique consectetur augue. Ut faucibus diam
ligula, eget porta elit dapibus ut. Praesent aliquam mollis felis finibus
sodales. Morbi dui diam, posuere sed ultricies sed, laoreet non lorem.

Nunc commodo, lectus id dignissim lobortis, lectus ex feugiat urna, a viverra
enim quam ut tortor. Aenean pellentesque id sapien ornare vehicula. Interdum et
malesuada fames ac ante ipsum primis in faucibus. Fusce diam sapien, maximus ut
malesuada sit amet, congue eu augue. Pellentesque sed metus quis nibh luctus
blandit in ut velit. Quisque eget massa purus. Vivamus vulputate pulvinar
sollicitudin. Curabitur tortor odio, dictum sed pulvinar at, consectetur
vulputate nulla. Nulla facilisi. Mauris sit amet consectetur ligula. Donec non
iaculis metus. Fusce ut erat maximus, fermentum purus sit amet, iaculis neque.
Fusce justo orci, finibus et feugiat eu, ullamcorper nec massa. Vivamus aliquam
semper pharetra.

Donec enim felis, suscipit vel sapien id, aliquam vestibulum neque. Donec sit
amet commodo ipsum. Nulla feugiat gravida sapien quis tristique. Nulla
facilisi. Vestibulum ut ultrices sapien, vel blandit dui. Vestibulum fringilla
tellus massa, vel facilisis leo accumsan vel. Ut sodales dui sapien, in
ullamcorper turpis ullamcorper vitae. Vivamus eu purus nec velit pulvinar
fringilla. In vel facilisis quam, sit amet ornare ex. Nulla feugiat ornare
vulputate. Praesent iaculis quam eget velit molestie pellentesque. Nulla id
libero aliquam, maximus leo nec, elementum metus. Vivamus lacinia nisl magna,
eget ullamcorper nunc interdum sit amet. Mauris quis scelerisque erat. Interdum
et malesuada fames ac ante ipsum primis in faucibus. Morbi vitae neque ac
ligula viverra dignissim.

Sed vulputate purus sit amet sapien suscipit sollicitudin. Ut aliquam lobortis
sem. Nam accumsan tempor purus vel vulputate. Praesent luctus libero est, sit
amet pulvinar libero maximus eget. Praesent tempor non elit congue elementum.
Donec tristique ipsum in ipsum viverra, eu blandit nulla tempus. Morbi mollis
in nisl ac rhoncus. Nullam rutrum, erat et venenatis vestibulum, mauris ligula
venenatis tortor, vel consectetur tellus orci eget odio. Etiam nec ligula sit
amet nunc ullamcorper volutpat. Ut blandit diam odio, nec pulvinar sem
fringilla eu. Fusce ut sem justo. Morbi ultricies hendrerit risus. Mauris
laoreet turpis lacus, non imperdiet dui pharetra a. Quisque placerat est sit
amet arcu mollis, eget porttitor tellus dictum. Morbi in euismod ex. Nullam ut
venenatis magna, non convallis lacus.

Mauris varius mi quis odio sagittis, vel vestibulum nisl mollis. Mauris enim
orci, porttitor quis sem in, dictum rhoncus nibh. Nulla mollis efficitur ex non
commodo. Cras elementum odio quam, at cursus arcu ullamcorper nec. Quisque
semper consequat nibh, et varius nulla vestibulum at. Aliquam erat volutpat.
Aenean non consequat lectus.

Ut metus diam, viverra eu hendrerit vitae, scelerisque nec velit. Proin lacinia
sem purus. Cras sed nisl ultricies justo facilisis ornare. Phasellus lectus
eros, eleifend sed nulla in, dapibus mollis nibh. Nunc tempor lacus in turpis
condimentum, ut placerat lectus pharetra. Maecenas eu commodo justo. Nam varius
varius nulla, sit amet sodales lectus gravida ut. Ut id mi urna. Aliquam nec
iaculis enim. Vestibulum nec imperdiet lectus, et imperdiet odio. Curabitur
hendrerit euismod quam, vitae volutpat metus. Donec tempor tristique pharetra.
Nullam sollicitudin, quam in laoreet interdum, lacus risus viverra magna, eget
dapibus velit odio at mi. In eget lobortis leo.

Fusce congue imperdiet pulvinar. Pellentesque posuere faucibus dolor congue
tempus. Aenean finibus orci vitae augue venenatis finibus et et orci. Maecenas
dictum ex augue, ut aliquet justo cursus et. Vivamus dolor ligula, vulputate
sit amet leo in, efficitur scelerisque sapien. Quisque rhoncus magna magna,
quis vulputate massa porta a. Maecenas luctus ex metus, eu viverra metus dictum
sed. Cras vehicula molestie risus, ullamcorper pellentesque mauris placerat
non. Cras nec condimentum mauris, quis commodo neque. Nullam est libero,
efficitur vitae augue a, tempus sagittis neque. Nam lobortis ultrices diam.
Etiam id nisl consectetur enim pulvinar suscipit. Aliquam in augue vel purus
vestibulum maximus. Fusce dapibus, felis eget condimentum aliquam, odio turpis
feugiat tellus, vitae porttitor odio nibh at nisi. In consectetur sapien in
enim tempor malesuada. Pellentesque habitant morbi tristique senectus et netus
et malesuada fames ac turpis egestas.

Morbi nec faucibus mauris, quis posuere ligula. Suspendisse venenatis nisl non
quam faucibus lobortis. Vestibulum iaculis dolor interdum urna mattis cursus.
Morbi ut commodo velit. Mauris tempus dictum auctor. Maecenas sed eros
pulvinar, suscipit lectus quis, luctus turpis. Donec vel elit non ipsum feugiat
faucibus. Phasellus tempor nulla condimentum ultricies interdum. Duis mattis
eleifend turpis tempus eleifend. Nam vehicula felis et sem tincidunt, vel
dignissim dolor vulputate. Etiam ut ornare ex. Curabitur at interdum tellus.

Aliquam consequat, nisi ut tempor suscipit, libero ipsum facilisis dolor, vitae
tincidunt justo ipsum in turpis. Morbi scelerisque lectus in velit feugiat,
quis fringilla purus suscipit. Cras risus lorem, euismod at mattis et,
efficitur mattis urna. Nunc nisl dolor, pellentesque vitae faucibus quis,
pharetra non est. Donec aliquet elit eget hendrerit maximus. Nam risus purus,
suscipit fringilla est at, accumsan cursus nunc. Suspendisse potenti.

Donec risus mauris, pulvinar ac nibh non, porta lacinia mauris. Maecenas
ultricies rhoncus nunc, et pretium lectus luctus vitae. Cras urna nulla,
suscipit ac commodo sed, vulputate at orci. Lorem ipsum dolor sit amet,
consectetur adipiscing elit. Donec facilisis tellus tortor, vel eleifend nibh
gravida sit amet. Morbi interdum lectus vel laoreet molestie. Curabitur quis
nisi id ante posuere auctor. Duis nec nibh convallis, efficitur nisl auctor,
aliquam elit. Ut consequat lectus vel felis congue faucibus. Cras quis tellus
magna.

Vestibulum rutrum sit amet neque sed scelerisque. Duis sit amet tellus orci.
Integer laoreet orci arcu, mollis dapibus dui pretium nec. Mauris nec orci non
metus mattis commodo. Nunc ac varius leo, non accumsan nulla. Aenean lobortis
ligula nibh, eu elementum sem lacinia a. Pellentesque dolor lorem, viverra vel
odio faucibus, efficitur porttitor ex. Aenean metus erat, condimentum ac dictum
id, viverra non nulla. Sed vitae pellentesque lectus. Aliquam dignissim justo a
volutpat tempor. Mauris nec libero auctor odio gravida molestie facilisis id
elit.

Duis pellentesque facilisis dictum. Integer molestie molestie enim, ac
facilisis dolor aliquam quis. In luctus rhoncus euismod. Curabitur nec mi
feugiat, commodo leo sit amet, condimentum metus. Nam finibus, sapien nec
tincidunt tristique, turpis nisl rhoncus quam, vitae finibus quam felis non
elit. Nullam ultrices fermentum mauris, sed ullamcorper est porta quis.
Praesent in nibh felis. Aliquam iaculis nulla sit amet nisl suscipit pulvinar.
Sed at posuere sapien. In consectetur justo vel lacus volutpat mattis et ut
velit. Morbi neque odio, pellentesque eu tincidunt et, ullamcorper eget nisi.
Donec vel rutrum felis, ac vestibulum diam. Vivamus euismod, enim nec
scelerisque hendrerit, mauris ante ultrices justo, id ultricies nisl magna at
nulla.

Curabitur auctor dolor et augue ultricies, in tincidunt urna consequat. Class
aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos
himenaeos. Sed placerat nisl blandit arcu venenatis ultricies. Suspendisse
gravida dictum nisl. Maecenas euismod risus non pulvinar condimentum. Interdum
et malesuada fames ac ante ipsum primis in faucibus. Etiam rhoncus iaculis
porttitor. Nullam lectus nisl, sollicitudin ac tortor ac, eleifend tempor
risus. Proin congue velit sed quam lobortis viverra. Morbi non magna nibh. Nunc
dapibus urna vel ex hendrerit, et interdum velit tincidunt. Duis euismod
blandit blandit.

Donec nec pellentesque risus, et sollicitudin risus. Nunc porttitor ultricies
odio nec fermentum. Proin sit amet massa non mi scelerisque aliquet. Aliquam
eleifend fringilla nunc, blandit blandit neque suscipit ac. Cras nunc erat,
vulputate nec est nec, molestie congue ipsum. Ut nec ultrices lacus. Proin ac
hendrerit eros. Nunc vel faucibus purus, in mattis lorem. Aliquam erat
volutpat. Curabitur sit amet venenatis lorem, sed consectetur purus. Aenean
diam ipsum, tincidunt id consectetur at, imperdiet vitae ex.

Donec dolor sapien, dignissim et condimentum id, laoreet vitae massa. Integer
ut nunc interdum eros maximus molestie in ut dui. Fusce suscipit purus non ex
pharetra, vitae fringilla ex rhoncus. Vestibulum dictum erat a massa bibendum,
sit amet sollicitudin dolor cursus. Proin odio massa, viverra sollicitudin nunc
sit amet, tempus mollis nulla. Suspendisse sed urna vitae quam consectetur
blandit ac ut ex. Vestibulum consequat finibus lectus ac varius. Vestibulum
eget ligula urna. Nam sit amet diam eros. Vestibulum aliquet, nunc et tristique
mattis, erat orci rutrum justo, ac mattis nunc ex et neque. Nunc vel elit
sagittis, varius lectus quis, efficitur mauris. Duis a sem diam. Suspendisse a
massa est. Proin non mauris eget arcu rutrum luctus. Phasellus metus neque,
ultrices nec egestas vel, faucibus bibendum ipsum.

Nulla tortor eros, congue vitae feugiat eu, vehicula id felis. In at ipsum
augue. Aliquam erat volutpat. Nullam ut purus metus. Ut in eleifend orci.
Praesent elementum, metus sed efficitur molestie, diam nisi consequat dui,
sagittis rutrum tellus risus eu arcu. Aenean eget pulvinar orci. Quisque eget
erat sed leo rhoncus feugiat eget at nisi. Sed eget pharetra lacus. Aenean
molestie justo eu metus auctor scelerisque. Nunc tempus ligula eget nisl
accumsan convallis. Nulla ex sapien, dictum quis dictum et, gravida in ipsum.
Cras elit turpis, scelerisque ut est sit amet, sodales commodo sapien. Aliquam
ipsum augue, efficitur eget libero sed, vestibulum lacinia ex. Maecenas auctor
orci id risus fringilla, lobortis scelerisque ipsum mattis. Sed ut est
lobortis, dictum magna vel, placerat arcu.

Praesent laoreet tincidunt eros. In in dolor tincidunt ante luctus malesuada.
Donec pulvinar ut turpis mattis lacinia. Donec pharetra bibendum imperdiet.
Morbi placerat accumsan rhoncus. Proin id nibh quam. Cras mollis dolor vel nunc
pretium, ac porttitor urna commodo. Integer ac mi molestie, dignissim elit sit
amet, cursus dui. Etiam quis porttitor ligula.

Duis hendrerit porta ex sit amet volutpat. Suspendisse eget magna malesuada,
ultricies felis ac, posuere lectus. Vestibulum ante ipsum primis in faucibus
orci luctus et ultrices posuere cubilia Curae; Maecenas porttitor libero
mauris, id mattis lacus sollicitudin vel. Suspendisse potenti. Duis nec arcu
sem. Vivamus in fermentum diam. In nunc enim, facilisis ut bibendum non,
sagittis dignissim eros. Aliquam dapibus eros eu risus euismod, in fringilla
turpis pretium. Fusce dapibus turpis lectus, non cursus lacus dignissim non.
Aenean in fringilla neque. Class aptent taciti sociosqu ad litora torquent per
conubia nostra, per inceptos himenaeos.

In egestas orci id massa faucibus pharetra. Donec vitae bibendum libero. Fusce
elementum ligula eu arcu mattis venenatis. Sed tempor est et placerat feugiat.
Etiam et mauris vel est luctus rhoncus id vel elit. Aliquam eleifend lobortis
scelerisque. Nunc id gravida ante, ut vulputate odio. Nunc tincidunt euismod
elit, in eleifend justo cursus ac. Morbi tempor leo libero, ultrices consequat
nisl auctor non. Quisque non aliquam lectus. Vivamus ac erat nulla. 

"""

class test_header(unittest.TestCase):
    def test_0(this):
        this.assertEqual(lexitar.decode_header(lexitar.encode_header(0)), 0)

    def test_12345(this):
        this.assertEqual(lexitar.decode_header(lexitar.encode_header(12345)), 12345)

    def test_5678(this):
        this.assertEqual(lexitar.decode_header(lexitar.encode_header(5678)), 5678)

class test_stream(unittest.TestCase):

    def test_small(this):
        data = b'small'
        packed = lexitar.pack_stream(data, 1)
        this.assertEqual(data, lexitar.unpack_stream(packed))

    def test_medium(this):
        data = b'This is a medium sized chunk of example data for testing lexitar'
        packed = lexitar.pack_stream(data, 1)
        this.assertEqual(data, lexitar.unpack_stream(packed))

    def test_big(this):
        data = ipsum.encode('ascii')
        packed = lexitar.pack_stream(data, 1)
        this.assertEqual(data, lexitar.unpack_stream(packed))


class test_translation(unittest.TestCase):
    def test_simple(this):
        data = b'This is a medium sized chunk of example data for testing lexitar'
        encoded = lexitar.encode_translate(data)
        this.assertEqual(data, lexitar.decode_translate(encoded))

class test_encode_decode(unittest.TestCase):
    def test_simple(this):
        data = b'This is a medium sized chunk of example data for testing lexitar'
        encoded = lexitar.encode(data)
        this.assertEqual(data, lexitar.decode(encoded))

    def test_ecc(this):
        ecc_rate = 0.1
        data = ipsum.encode('ascii')
        encoded = lexitar.encode(data, 72, ecc_rate).split()
        #  print(encoded)
        #  errors = int(ecc_rate * len(data) * 0.2 - 2)
        errors = 0
        for i in range(errors):
            encoded[(65 + i) % len(encoded)] = "test_error"
        encoded = ' '.join(encoded)
        this.assertEqual(data, lexitar.decode(encoded))

class rs_sanity(unittest.TestCase):
    def test_rs_small(this):
        rs = reedsolo.RSCodec(12)
        data = b'This is a medium sized chunk of example data for testing lexitar'
        this.assertEqual(rs.decode(rs.encode(data)), data)

    def test_rs_big(this):
        rs = reedsolo.RSCodec(10)
        data = ipsum.encode('ascii')
        this.assertEqual(rs.decode(rs.encode(data)), data)

if __name__ == '__main__':
    unittest.main()
