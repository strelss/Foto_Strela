from django.db import models

class Gallery_Famyly(models.Model):
    fam_img1 = models.ImageField(upload_to='media/fam')
    fam_img2 = models.ImageField(upload_to='media/fam')
    fam_img3 = models.ImageField(upload_to='media/fam')
    fam_img4 = models.ImageField(upload_to='media/fam')
    fam_img5 = models.ImageField(upload_to='media/fam')
    fam_img6 = models.ImageField(upload_to='media/fam')

    class Meta:
        verbose_name = 'Семейная фотография'
        verbose_name_plural = 'Семейные фотографии'

class Gallery_Portrait(models.Model):
    port_img1 = models.ImageField(upload_to='media/por')
    port_img2 = models.ImageField(upload_to='media/por')
    port_img3 = models.ImageField(upload_to='media/por')
    port_img4 = models.ImageField(upload_to='media/por')
    port_img5 = models.ImageField(upload_to='media/por')
    port_img6 = models.ImageField(upload_to='media/por')

    class Meta:
        verbose_name = 'Портрет'
        verbose_name_plural = 'Портреты'

class Gallery_Weding(models.Model):
    wed_img1 = models.ImageField(upload_to='media/wed')
    wed_img2 = models.ImageField(upload_to='media/wed')
    wed_img3 = models.ImageField(upload_to='media/wed')
    wed_img4 = models.ImageField(upload_to='media/wed')
    wed_img5 = models.ImageField(upload_to='media/wed')
    wed_img6 = models.ImageField(upload_to='media/wed')

    class Meta:
        verbose_name = 'Свадебная фотография'
        verbose_name_plural = 'Свадебные фотографии'

