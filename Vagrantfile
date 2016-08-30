VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define :athena do |x|
    x.vm.box = "hashicorp/precise64"

    x.vm.provider :virtualbox do |v|
      v.name = "athena"
    end

    x.vm.provider :aws do |aws, override|
      aws.access_key_id = ENV['AWS_KEY']
      aws.secret_access_key = ENV['AWS_SECRET']
      aws.keypair_name = ENV['AWS_KEYNAME']
      aws.security_groups = ['applications']
      aws.ami = "ami-7747d01e"
      aws.region = "us-east-1"
      aws.instance_type = "m3.medium"

      override.vm.box = "dummy"
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = ENV['AWS_KEYPATH']
    end
  end

  config.vm.provision "shell", path: "provision.sh", env: ENV
end