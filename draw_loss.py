import os
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})

class LossHistory():
    def __init__(self, log_dir, val_loss_flag=True):
        self.log_dir        = log_dir
        self.val_loss_flag  = val_loss_flag

        self.losses         = self.read_losses_from_file("/epoch_loss.txt")
        if self.val_loss_flag:
            self.val_loss   = self.read_losses_from_file("/epoch_val_loss.txt")

    def read_losses_from_file(self, filename):
        with open(os.path.join(self.log_dir, filename), 'r') as f:
            losses = [float(line.strip()) for line in f]
        return losses

    def loss_plot(self):
        iters = range(len(self.losses))

        plt.figure()
        plt.plot(iters, self.losses, 'red', linewidth = 2, label='train loss')
        if self.val_loss_flag:
            plt.plot(iters, self.val_loss, 'coral', linewidth = 2, label='val loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.savefig(os.path.join(self.log_dir, "loss_plot.png"))

# 使用方法
log_dir = "/Loss_Plot"
history = LossHistory(log_dir)
history.loss_plot()