

    def generator_loss(self, Ra, loss_func, real, fake):
        fake_loss = 0
        real_loss = 0

        if Ra and loss_func.__contains__('wgan') :
            #print("No exist [Ra + WGAN], so use the {} loss function".format(loss_func))
            Ra = False

        if Ra :
            real_logit = (real - tf.reduce_mean(fake))
            fake_logit = (fake - tf.reduce_mean(real))

            if loss_func == 'lsgan' :
                real_loss = tf.reduce_mean(tf.square(real_logit + 1.0))
                fake_loss = tf.reduce_mean(tf.square(fake_logit - 1.0))

            if loss_func == 'gan' or loss_func == 'gan-gp' or loss_func == 'dragan' :
                print('G ra_en sigmoid loss')
                real_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=tf.zeros_like(real), logits=real_logit))
                fake_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=tf.ones_like(fake), logits=fake_logit))

            if loss_func == 'ngan' :
                print('G ra_en softmax loss')
                real_loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=tf.zeros_like(real), logits=real_logit))
                fake_loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=tf.ones_like(fake), logits=fake_logit))

            if loss_func == 'hinge' :
                real_loss = tf.reduce_mean(tf.nn.relu(1.0 + real_logit))
                fake_loss = tf.reduce_mean(tf.nn.relu(1.0 - fake_logit))

        else :
            if loss_func == 'wgan-gp' or loss_func == 'wgan-lp':
                fake_loss = -tf.reduce_mean(fake)

            if loss_func == 'lsgan' :
                fake_loss = tf.reduce_mean(tf.square(fake - 1.0))

            if loss_func == 'gan' or loss_func == 'gan-gp' or loss_func == 'dragan' :
                print('G ra_off sigmoid loss')
                fake_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=tf.ones_like(fake), logits=fake))

            if loss_func == 'ngan':
                print('G ra_off softmax loss')
                fake_loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=tf.ones_like(fake), logits=fake))

            if loss_func == 'hinge' :
                fake_loss = -tf.reduce_mean(fake)

        loss = fake_loss + real_loss

        return loss
