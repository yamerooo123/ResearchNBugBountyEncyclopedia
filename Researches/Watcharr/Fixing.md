/DATA allows read but not write privileges

the folder is designed to be accessed only to high privileged users (sudo privilege) as it containing sensitive data which is why when JWT try to read JWT_SECRET, it couldn't retrieve because it lacks the privilege. This vulnerability has to do with Design Flaw.
