# Задание 4

Поиск объекта по шаблону, так как roboflow распознает объекты при небольших датасетах (< 1000) не лучшим образом, рассмотрим еще два варианта нахождения нужного объекта

OpenCV: Template Matching, - использовать встроенную функцию opencv. Недостаток, повернутый объект не найдет.

Mask R-CNN Object Counting API https://github.com/ahmetozlu/tensorflow_object_counting_api/tree/master/mask_rcnn_counting_api Недостаток, сложнее запустить, будет зависеть от ПК tf.Session заменяем на tf.compat.v1.Session 

Датасеты для сравнения по маске можно посмотреть тут COCO - Common Objects in Context (cocodataset.org)

